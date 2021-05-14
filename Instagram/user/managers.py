from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy


class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, username, **extra_fields):
        if not email:
            # ugettext_lazy() will convert english into any other language "Language Conversion"
            raise ValueError(ugettext_lazy('The Email must be set.'))

        # Normalizing the email field
        email = self.normalize_email(email)
        user = self.model(email=email, username= username,  **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, username, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            return ValueError(ugettext_lazy('The Superuser must have is_staff = True.'))
        if extra_fields.get('is_superuser') is not True:
            return ValueError(ugettext_lazy('The Superuser must have is_superuser = True.'))
        return self.create_user(email, password, **extra_fields)
