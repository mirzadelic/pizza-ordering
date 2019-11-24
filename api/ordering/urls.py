from django.urls import path, include
from rest_framework import routers

from .views import OrderView


router = routers.SimpleRouter()
router.register(r'order', OrderView)

app_name = 'ordering'
urlpatterns = [
    path('', include(router.urls)),
]
