from django import forms
from .models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class UserCreateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'first_name', 'last_name')

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd.get("password") and cd.get("password_confirm") and cd["password"] != cd['password_confirm']:
            raise ValidationError('passwords don"t match')
        return cd["password_confirm"]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text=
                                         'you can change password using <a href=\"../password/\">this form</a>')

    class Meta:
        model = User
        fields = ('email', 'phone_number', 'password', 'first_name', 'last_name')
