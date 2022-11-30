from rest_framework.serializers import ModelSerializer

from projects.models import Contributor, Issue, Project

class ProjectSerializer(ModelSerializer):
      
      class Meta:
            model = Project
            fields = ['id', 'title', 'description', 'type', 'author_user_id',]
            
            
            
class ContributorSerializer(ModelSerializer):

    class Meta:
        model = Contributor
        fields = ['id', 'user_id', 'project_id']            
            

class IssueSerializer(ModelSerializer):
      
      class Meta:
        model = Issue
        fields = [
            "id",
            "title",
            "description",
            "tag",
            "priority",
            "status",
            "project_id",
            "author_user_id",
            "assignee_user_id",
            "created_time",
        ]  
        