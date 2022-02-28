from django.urls import path

from .views.carts import CartAddView, CartIndexView, CartDeleteView
from .views.orders import OrderView, MyOrderView
from .views import ProductIndexView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductIndexView.as_view(), name="product_index"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/add/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete"),
    path('cart/product/<int:pk>/add', CartAddView.as_view(), name='cart_add'),
    path('cart/', CartIndexView.as_view(), name='cart_view'),
    path('cart/product/<int:pk>/delete', CartDeleteView.as_view(), name='cart_delete'),
    path('order/', OrderView.as_view(), name='order_view'),
    path('myorders/', MyOrderView.as_view(), name='my_order_view')
]
