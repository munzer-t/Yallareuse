from django.urls import path

from .views import create_product_view, product_detail_view, product_list_view

urlpatterns = [
    path('create/', create_product_view, name='create_product'),
    path('all/', product_list_view, name='product_list_initial'),
    path('all/<int:category>/', product_list_view, name='product_list'),
    path('detail/<int:product>/', product_detail_view, name='product_detail')
]