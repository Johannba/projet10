from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import include, path
from django.contrib import admin
from user.views import RegisterApi
from projects.views import (
    CommentViewSet,
    ContributorViewSet,
    IssueViewSet,
    ProjectViewSet,
)


router = routers.SimpleRouter(trailing_slash=True)
router.register(r"project/?", ProjectViewSet, basename="project")

users_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
users_router.register(r"users/?", ContributorViewSet, basename="users")

issue_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
issue_router.register(r"issue/?", IssueViewSet, basename="issue")

comment_router = routers.NestedSimpleRouter(issue_router, r"issue/?", lookup="issue")
comment_router.register(r"comment/?", CommentViewSet, basename="comment")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", RegisterApi.as_view(), name="signup"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path(r'', include(router.urls)),
    path(r'', include(users_router.urls)),
    path(r'', include(issue_router.urls)),
    path(r'', include(comment_router.urls)),
]
