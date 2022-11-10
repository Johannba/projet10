from django.conf import settings
from django.db import models


class Projects(models.Model):
      project_id = models.IntegerField()
      title = models.CharField(max_length=155)
      description = models.CharField(max_length=5000)
      type = models.CharField(max_length=12)
      author_user_id = models.ForeignKey(
            to=settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)