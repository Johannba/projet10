from rest_framework import routers

from projects.views import ProjectsViewset


router = routers.SimpleRouter()
router.register('projects', ProjectsViewset, basename='projects')