from rest_framework.serializers import ModelSerializer

from projects.models import Contributor, Project

class ProjectSerializer(ModelSerializer):
      
      class Meta:
            model = Project
            fields = ['title', 'description', 'type', 'author_user_id',]
            
            
            
class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id']            
            