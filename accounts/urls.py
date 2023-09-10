from django.urls import path
from . import views

app_name = "accounts"
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('verify/', views.UserRegisterVerifyCodeView.as_view(), name='verify'),
    path('logout/', views.UserLogoutView.as_view(), name="logout"),
    path('login/', views.UserLoginView.as_view(), name="login"),
]