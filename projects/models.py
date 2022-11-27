from django.conf import settings
from django.db import models


class Project(models.Model):
      title = models.CharField(max_length=155)
      description = models.CharField(max_length=5000)
      type = models.CharField(max_length=12)
      author_user_id = models.ForeignKey(
            to=settings.AUTH_USER_MODEL,
            on_delete=models.CASCADE)
      

class Contributor(models.Model):
      user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
      project_id = models.ForeignKey(to=Project, on_delete=models.CASCADE)
      
      class Meta:
        unique_together = ('project_id', 'user_id')
        