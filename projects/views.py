from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q

from projects.models import Comment, Contributor, Issue, Project
from projects.serializers import (
    CommentSerializer,
    ContributorSerializer,
    IssueSerializer,
    ProjectSerializer,
)

from projects.permission import (
    IsContributorOrAuthorProjectInProjectView,
    ContributorViewsetPermission,
    issueViewsetPermission,
    CommentViewsetPermission,
)


class ProjectViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated, IsContributorOrAuthorProjectInProjectView]

    def get_queryset(self):
        return Project.objects.filter(
            Q(author_user_id=self.request.user.id)
            | Q(contributor__user_id=self.request.user.id)
        )

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
    serializer_class = ContributorSerializer
    http_method_names = ["get", "post", "delete"]
    permission_classes = [IsAuthenticated, ContributorViewsetPermission]

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
    permission_classes = [IsAuthenticated, issueViewsetPermission]

    def get_queryset(self):
        return Issue.objects.filter(project_id=self.kwargs["project__pk"])

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


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = [IsAuthenticated, CommentViewsetPermission]

    def get_queryset(self):
        return Comment.objects.filter(issue_id=self.kwargs["issue__pk"])

    # Récupérer la liste de tous les commentaires liés à un problème (issue)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = self.kwargs["issue__pk"]
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["issue_id"] = self.kwargs["pk"]
        request.data["author_user_id"] = request.user.pk
        request.POST._mutable = False
        return super(CommentViewSet, self).update(request, *args, **kwargs)
