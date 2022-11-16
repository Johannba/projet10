from rest_framework.response import Response 
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from projects.models import Projects
from projects.serializers import ProjectsSerializer

class ProjectsViewset(ReadOnlyModelViewSet):
      
      serializer_class = ProjectsSerializer
      
      def get_queryset(self):
            return Projects.objects.all()
      
      def get(self, *args, **kwargs):
            queryset = Projects.objects.all()
            serializer = ProjectsSerializer(queryset, many=True)
            return Response(serializer.data)