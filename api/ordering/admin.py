from django.contrib import admin

from .models import PizzaOrder, Order, PizzaOrderDetails


class PizzaOrderInline(admin.TabularInline):
    model = PizzaOrder


class PizzaOrderDetailsInline(admin.TabularInline):
    model = PizzaOrderDetails


class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status')

    inlines = [
        PizzaOrderInline,
    ]


class PizzaOrderAdmin(admin.ModelAdmin):
    list_display = ('order', 'flavor')

    inlines = [
        PizzaOrderDetailsInline,
    ]


admin.site.register(PizzaOrder, PizzaOrderAdmin)
admin.site.register(Order, OrderAdmin)
