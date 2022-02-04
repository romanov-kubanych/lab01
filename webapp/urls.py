from django.urls import path


from webapp.views import index_view, ProductDetailView, create_view, update_view, ProductDeleteView

urlpatterns = [
    path('', index_view, name="product_index"),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_view'),
    path('product/add/', create_view, name='product_create'),
    path('product/<int:pk>/update', update_view, name='product_update'),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete")
]
