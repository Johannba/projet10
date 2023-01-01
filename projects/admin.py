from . import models
from django.contrib import admin

admin.site.register(models.Comment)
admin.site.register(models.Contributor)
admin.site.register(models.Issue)
admin.site.register(models.Project)

# Register your models here.
