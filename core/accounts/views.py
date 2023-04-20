from django.shortcuts import (
    render,
    redirect,
)
from django.views import View
from .forms import (
    UserRegistrationForm,
    VerifyCodeForm
)
from ..utils import send_otp_code
from models import (
    OtpCode,
    User,
)
from django.contrib import messages
import random


class UserRegisterView(View):
    form_class = UserRegistrationForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, 'accounts/register.html', {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(0, 9999)
            send_otp_code(form.cleaned_data["phone_number"], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data["phone_number"], code=random_code)
            request.session["user_register_info"] = {
                "phone_number": form.cleaned_data["phone_number"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "username": form.cleaned_data["username"],
                "password": form.cleaned_data["password"]
            }
            messages.success(request, "we send you code ", "success")
            redirect("accounts:verify_code")
        redirect("home:home")


class UserRegisterVerifyCode(View):
    form_class = VerifyCodeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, "accounts/verify.html", {"form": form})

    def post(self, request, *args, **kwargs):
        user_session = request.session["user_register_info"]
        otp_obj = OtpCode.objects.get(phone_number=user_session["phone_number"])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd["code"] == otp_obj.code:
                User.objects.create_user(phone_number=user_session["phone_number"],
                                         email=user_session["email"],
                                         first_name=user_session["first_name"],
                                         last_name=user_session["last_name"],
                                         password=user_session["password"]

                )
                otp_obj.delete()
                messages.success(request, "you register successfully", "success")
                redirect("home:home")
            else:
                messages.error(request, "this is code wrong", 'danger')
                redirect("accounts:verify")

        redirect("home:home")


