from rest_framework.test import APIClient, APITestCase

from django.urls import reverse

from .models import Order, PizzaOrder, PizzaOrderDetails


class OrderViewTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.url = reverse('api:ordering:order-list')

        self.order = Order.objects.create(
            status=1,
            customer={
                'name': 'Test',
                'address': 'Address',
                'phone': 'Phone'
            })

    def test_get_success(self):
        response = self.client.get(self.url)

        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.status_code, 200)

    def test_post_success(self):
        data = {
            'customer': {
                'name': 'asd',
                'address': 'www',
                'phone': 'ewfds'
            },
            'pizza': [
                {
                    'flavor': 2,
                    'details': [
                        {
                            'size': 1,
                            'quantity': 2
                        }
                    ]
                }
            ],
            'status': 1
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(Order.objects.count(), 2)

    def test_put_success(self):
        data = {
            'customer': {
                'name': 'asd',
                'address': 'www',
                'phone': 'ewfds'
            },
            'pizza': [
                {
                    'flavor': 2,
                    'details': [
                        {
                            'size': 1,
                            'quantity': 2
                        }
                    ]
                }
            ],
            'status': 1
        }

        response = self.client.put(
            reverse('api:ordering:order-detail', kwargs={'pk': self.order.pk}),
            data=data
        )

        self.assertEqual(response.status_code, 200)

        order = Order.objects.get(pk=self.order.pk)
        self.assertEqual(order.customer['name'], data['customer']['name'])
        self.assertEqual(order.customer['address'], data['customer']['address'])
        self.assertEqual(order.customer['phone'], data['customer']['phone'])

        self.assertEqual(order.pizza.count(), 1)

    def test_put_status_only_change(self):
        self.order.status = 2
        self.order.save()
        data = {
            'customer': {
                'name': 'asd',
                'address': 'www',
                'phone': 'ewfds'
            },
            'pizza': [
                {
                    'flavor': 2,
                    'details': [
                        {
                            'size': 1,
                            'quantity': 2
                        }
                    ]
                }
            ],
            'status': 1
        }

        response = self.client.put(
            reverse('api:ordering:order-detail', kwargs={'pk': self.order.pk}),
            data=data
        )

        self.assertEqual(response.status_code, 200)

        order = Order.objects.get(pk=self.order.pk)
        self.assertEqual(order.status, data['status'])
        self.assertEqual(order.customer['name'], 'Test')
        self.assertEqual(order.customer['address'], 'Address')
        self.assertEqual(order.customer['phone'], 'Phone')
