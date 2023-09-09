from django.urls import path
from . import views

app_name = "product"

urlpatterns = [
    path('', views.ProductView.as_view(), name='products'),
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('category/<slug:category_slug>/', views.ProductView.as_view(), name='category_filter'),
]
