from django.shortcuts import render
from django.views.generic import TemplateView

from rest_framework.response import Response 
from rest_framework.views import APIView

from projects.models import Projects
from projects.serializers import ProjectsSerializer


class HomeView(TemplateView):
      template_name = 'base.html'


def home_view(requests):
      return render(requests, 'base.html', context={
            'title':'Acceuil',
      })

class ProjectsView(APIView):
      
      def get(self, *args, **kwargs):
            queryset = Projects.objects.all()
            serializer = ProjectsSerializer(queryset, many=True)
            return Response(serializer.data)