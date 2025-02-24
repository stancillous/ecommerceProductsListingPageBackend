from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.products_view, name="products view"),
    # path('products/:<str:slug>/', views.specific_product_view, name="specific product view"),
    path('products/<int:id>/', views.get_product_by_id, name="get product by id")   
    
]