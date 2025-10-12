from django.urls import path
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('create_product',views.create_product,name='create_product'),
    path('product_list',views.product_list,name='product_list'),
    path('update_product/<int:id>',views.update_product,name='update_product'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product')
    #127.0.0.1:8000/api/home
]
