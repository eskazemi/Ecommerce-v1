from django.urls import (
    path,
    include,
)
from . import views

app_name = "product"


bucket_urls = [
    path('', views.BucketView.as_view(), name='bucket'),
    path('delete/<str:key>', views.DeleteBucketView.as_view(), name='delete_bucket'),
    path('download/<str:key>/', views.DownloadBucketView.as_view(), name='download_bucket')
]
urlpatterns = [
    path('',  views.ProductView.as_view(), name='products'),
    path('detail/<slug:slug>/',  views.ProductDetailView.as_view(), name='product_detail'),
    path('bucket/', include(bucket_urls))
]
