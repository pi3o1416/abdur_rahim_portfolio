
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def clean(self, *args, **kwargs):
        if User.objects.all().exists():
            raise ValidationError("Database only allow one user")
        super().clean(*args, **kwargs)






