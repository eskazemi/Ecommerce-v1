from django.shortcuts import (
    render,
    redirect,
)
from django.views import View
from . import tasks
from django.contrib import messages
from utils import ISAdminUser


class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'home/home.html')


class BucketView(ISAdminUser, View):
    template_name = 'home/bucket.html'

    def get(self, request, *args, **kwargs):
        objects = tasks.all_buckets_objects_task()
        return render(request, self.template_name, {"objects": objects})


class DeleteBucketView(ISAdminUser, View):

    def get(self, request, key, *args, **kwargs):
        tasks.delete_object_task.delay(key)
        messages.success(request, 'your object will be delete soon', 'success')
        return redirect('home:bucket')


class DownloadBucketView(ISAdminUser, View):
    def get(self, request, key, *args, **kwargs):
        tasks.download_object_task.delay(key)
        messages.success(request, 'your object will be download soon', 'success')
        return redirect('home:bucket')
