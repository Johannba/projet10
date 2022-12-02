
from rest_framework.viewsets import ModelViewSet

from projects.models import Comment, Contributor, Issue, Project
from projects.serializers import CommentSerializer, ContributorSerializer, IssueSerializer, ProjectSerializer

from user.serializers import UserSerializer

class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "put", "delete"]
    
    def get_queryset(self):
        return Project.objects.all()
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(ProjectViewSet, self).update(request, *args, **kwargs)


   
class ContributorViewSet(ModelViewSet):
    serializer_class =  ContributorSerializer
    http_method_names = ["get", "post", "delete"]
    
    def get_queryset(self):
        return Contributor.objects.filter(project_id=self.kwargs["project__pk"])
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project__pk"] 
        request.POST._mutable = False
        return super(ContributorViewSet, self).create(request, *args, **kwargs)
    
class IssueViewSet(ModelViewSet):
    serializer_class = IssueSerializer
    http_method_names = ["get", "post", "put", "delete"]
    
    def get_queryset(self):
        return Issue.objects.all()
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project__pk"] 
        request.data["author_user_id"] = request.user.pk
        request.data["assignee_user"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewSet, self).create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["project_id"] = self.kwargs["project__pk"] 
        request.data["author_user_id"] = request.user.pk
        request.data["assignee_user"] = request.user.pk
        request.POST._mutable = False
        return super(IssueViewSet, self).update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return super(IssueViewSet, self).delete(request, *args, **kwargs)
        
    
    
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    
    def get_queryset(self):
        return Comment.objects.all()
    
    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = self.kwargs["project__pk"] 
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = self.kwargs["project__pk"] 
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).update(request, *args, **kwargs)