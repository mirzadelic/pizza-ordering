from rest_framework import serializers

from .models import Order, PizzaOrder, PizzaOrderDetails


class CustomerSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, trim_whitespace=True)
    address = serializers.CharField(max_length=200, trim_whitespace=True)
    phone = serializers.CharField(max_length=30, trim_whitespace=True)

    class Meta:
        fields = '__all__'


class PizzaOrderDetailsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)

    class Meta:
        model = PizzaOrderDetails
        fields = ('id', 'size', 'quantity')


class PizzaOrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    details = PizzaOrderDetailsSerializer(many=True)

    class Meta:
        model = PizzaOrder
        fields = ('id', 'flavor', 'details')


class OrderSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    customer = CustomerSerializer()
    pizza = PizzaOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = '__all__'

    @classmethod
    def create_or_update_pizza_order_details(cls, pizza_order, details):
        details_pks = []
        for d in details:
            if 'id' in d:
                pizza_details_obj = PizzaOrderDetails.objects.get(pk=d['id'])
            else:
                pizza_details_obj = PizzaOrderDetails(pizza_order=pizza_order)

            pizza_details_obj.size = d['size']
            pizza_details_obj.quantity = d['quantity']
            pizza_details_obj.save()
            details_pks.append(pizza_details_obj.pk)

        if details_pks:
            PizzaOrderDetails.objects.exclude(pk__in=details_pks).delete()

    @classmethod
    def create_or_update_pizza_order(cls, order, pizza):
        pizza_pks = []
        for p in pizza:
            if 'id' in p:
                pizza_obj = PizzaOrder.objects.get(pk=p['id'])
            else:
                pizza_obj = PizzaOrder(order=order)

            pizza_obj.flavor = p['flavor']
            pizza_obj.save()
            pizza_pks.append(pizza_obj.pk)

            cls.create_or_update_pizza_order_details(pizza_obj, p['details'])

        if pizza_pks:
            PizzaOrder.objects.exclude(pk__in=pizza_pks).delete()

    def create(self, validated_data):
        pizza = validated_data.pop('pizza', [])
        customer = validated_data.pop('customer', {})

        order = super().create(validated_data)
        order.customer = customer
        order.save()

        self.create_or_update_pizza_order(order, pizza)

        return order

    def update(self, order, validated_data):
        pizza = validated_data.pop('pizza', [])
        customer = validated_data.pop('customer', {})

        if order.status != 1:
            order.status = validated_data['status']
            order.save()
        else:
            order = super().update(order, validated_data)
            order.customer = customer
            order.save()

            self.create_or_update_pizza_order(order, pizza)

        return order
