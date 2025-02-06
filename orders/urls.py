from django.urls import path
from .views import create_order, order_list, view_order

urlpatterns = [
    path('create/', create_order, name='create_order'),
    path('my-orders/', order_list, name='order_list'),
    path('order/<int:order_id>/', view_order, name='view_order'),
]