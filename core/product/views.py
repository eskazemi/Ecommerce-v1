from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)
from django.views import View
from .models import Product
from . import tasks
from django.contrib import messages


class ProductView(View):
    def get(self, request, *args, **kwargs):
        products = Product.objects.filter(is_available=True)
        return render(request, 'product/index.html', {"products": products})


class ProductDetailView(View):

    def get(self, request, slug, *args, **kwargs):
        product = get_object_or_404(Product, slug=slug)
        return render(request, 'product/detail.html', {'product': product})


class BucketView(View):
    template_name = 'product/bucket.html'

    def get(self, request, *args, **kwargs):
        objects = tasks.all_buckets_objects_task()
        return render(request, self.template_name, {"objects": objects})


class DeleteBucketView(View):

    def get(self, request, key, *args, **kwargs):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your object will be delete soon', 'success')
        return redirect('product:bucket')


class DownloadBucketView(View):
    def get(self, request, key, *args, **kwargs):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your object will be download soon', 'success')
        return redirect('product:bucket')
