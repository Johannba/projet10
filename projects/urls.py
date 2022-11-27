from rest_framework_nested import routers

from projects.views import ContributorViewSet, ProjectViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r"project/?", ProjectViewSet, basename='project')

users_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
users_router.register(r"users/?",ContributorViewSet, basename="users")