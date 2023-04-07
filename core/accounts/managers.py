from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, phone_number, email, first_name, last_name, password):
        if not phone_number:
            raise ValueError('user must have phone number')
        if not email:
            raise ValueError('user must have email')

        if not first_name or not last_name:
            raise ValueError('user nust have first_name and last_name')

        user = self.model(phone_number=phone_number, email=self.normalize_email(email), first_name=first_name,
                          last_name=last_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, email, first_name, last_name, password):
        user = self.create_user(phone_number=phone_number, email=email, first_name=first_name
                                , last_name=last_name, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user
