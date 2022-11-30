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
        
        
class Issue(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=5000)
    created_time = models.DateTimeField(auto_now_add=True)

    priority = models.CharField(max_length=12)
    tag = models.CharField(max_length=12) 
    status = models.CharField(max_length=12)       
    
    
    author_user_id = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='issue_author')

    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=author_user_id,
        related_name='issue_assignee')

    project_id = models.ForeignKey(
        to=Project,
        on_delete=models.CASCADE,
        related_name='issues'
    )