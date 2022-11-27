
from rest_framework.viewsets import ModelViewSet

from projects.models import Contributor, Project
from projects.serializers import ContributorSerializer, ProjectSerializer

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
    serializer_class =  UserSerializer
    http_method_names = ["get", "post", "put", "delete"]
    
    def get_queryset(self):
        return Contributor.objects.all()
    
    def create(self, request, *args, **kwargs):
        print(kwargs)
        request.POST._mutable = True
        request.data["project"] = self.kwargs["project_pk"]
        request.POST._mutable = False
        return super(ContributorViewSet, self).create(request, *args, **kwargs)
    
