from django.contrib.auth.models import AbstractUser
from django.db.models import EmailField, BooleanField


class CustomUser(AbstractUser):
    email = EmailField(unique=True)
    is_email_verified = BooleanField(default=False)

    def __str__(self):
        return self.username
