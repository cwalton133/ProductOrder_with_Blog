from django.urls import path
from .views import (
    product_list,
    product_detail,
    product_create,
    product_update,
    product_delete,
)

urlpatterns = [
    path('', product_list, name='product_list'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('product/new/', product_create, name='product_create'),
    path('product/<int:pk>/edit/', product_update, name='product_update'),
    path('product/<int:pk>/delete/', product_delete, name='product_delete'),
]