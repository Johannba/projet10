
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status,response

from projects.models import Projects
from projects.serializers import ProjectsSerializer

class ProjectsViewset(ReadOnlyModelViewSet):
      
      serializer_class = ProjectsSerializer
      
      def get_queryset(self):
            return Projects.objects.all()
      
      def create(self, request, *args, **kwargs):
        project = Projects(author_user_id=request.user.id)
        data = request.data.copy()
        data['author_user_id'] = request.user.id
        serializer = self.serializer_class(project, data=data)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)