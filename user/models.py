from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    # Disable username field and enable login via email
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # Make a new member active & staff by default, so it can do CRUD operations
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
