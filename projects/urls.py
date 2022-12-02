from rest_framework_nested import routers

from projects.views import CommentViewSet, ContributorViewSet, IssueViewSet, ProjectViewSet


router = routers.SimpleRouter(trailing_slash=False)
router.register(r"project/?", ProjectViewSet, basename='project')

users_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
users_router.register(r"users/?",ContributorViewSet, basename="users")

issue_router = routers.NestedSimpleRouter(router, r"project/?", lookup="project")
issue_router.register(r"issue/?",IssueViewSet, basename="issue")

comment_router = routers.NestedSimpleRouter(issue_router, r"issue/?", lookup="issue")
comment_router.register(r"comment/?",CommentViewSet, basename="comment")