from django.urls import path

from webapp.views import index_view, product_view, create_view, update_view, delete_view

urlpatterns = [
    path('', index_view, name="index_view"),
    path('product/<int:pk>/', product_view, name='product_view'),
    path('product/add/', create_view, name='create_view'),
    path('product/<int:pk>/update', update_view, name='update_view'),
    path('product/<int:pk>/delete', delete_view, name="delete_view")
]
