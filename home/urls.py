from django.urls import path
from . import views

app_name = "home"
urlpatterns = [
    path('',  views.HomeView.as_view(), name='home'),
    path('bucket', views.BucketView.as_view(), name='buckets'),
    path('bucket/delete/<str:key>', views.DeleteBucketView.as_view(), name='delete_bucket'),
    path('bucket/download/<str:key>/', views.DownloadBucketView.as_view(), name='download_bucket')
]
