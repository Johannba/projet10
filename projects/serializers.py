from rest_framework.serializers import ModelSerializer

from projects.models import Projects

class ProjectsSerializer(ModelSerializer):
      
      class Meta:
            model = Projects
            fields = ['project_id', 'title', 'description', 'type', 'author_user_id',]