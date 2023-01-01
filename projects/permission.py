from projects import models
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

# verifie si l' autheur est la personne connecter
User = get_user_model()

def is_author(pk, user):
    # verifie si projet existe
    try:
        content = models.Project.objects.get(pk=pk)
        print(content.author_user_id)
        print(user)
    except ObjectDoesNotExist:
        # si existe pas exption qui retourne faux
        return False
    # si vrai on fait apparaitre l'autheur_user_id == a celui connecter(user)
    return content.author_user_id == user

    # vérifie si pers connecte est contributeur de tel projet


def is_contributor(pk, user):
    # vérifie si contributeur le user_id = user , projet_id=pk
    # added 
    user = User.objects.get(username=user)
    project = models.Project.objects.get(id=pk)
    print(user.username)
    print(project)
    try:
        contrib = models.Contributor.objects.filter(user_id=user, project_id=project)
    except ObjectDoesNotExist:
        return False
    return True


def is_author_comment(pk, user):
    # verifie si projet existe
    try:
        content = models.Comment.objects.get(pk=pk)
        print("content : ", content)
    except ObjectDoesNotExist:
        # si existe pas exption qui retourne faux
        print("Exception is author")
        return False
    # si vrai on fait apparaitre l'autheur_user_id == a celui connecter(user)
    print("user : ", content.author_user_id, user)
    return content.author_user_id == user


class IsContributorOrAuthorProjectInProjectView(permissions.BasePermission):
    # surcharge la methode has_permission qui retourne toujours vrai
    def has_permission(self, request, view):
        #     si l'action = create on retourne vrai
        if view.action == "create":
            return True
        # si action
        if view.action in ("destroy", "update"):
            return is_author(view.kwargs["pk"], request.user)
        try:
            is_author_or_contibutor = is_author(
                view.kwargs["pk"], request.user
            ) or is_contributor(view.kwargs["pk"], request.user)
        except KeyError:
            return True
        return is_author_or_contibutor


class ContributorViewsetPermission(permissions.BasePermission):
    # surcharge la methode has_permission qui retourne toujours vrai
    def has_permission(self, request, view):
        #     si l'action = create on retourne vrai
        # si action
        if view.action in ("destroy", "update", "create"):
            return is_author(view.kwargs["project__pk"], request.user)
        try:
            is_author_or_contributor = is_author(
                view.kwargs["project__pk"], request.user
            ) or is_contributor(view.kwargs["project__pk"], request.user)
        except KeyError:
            return True
        return is_author_or_contributor


class issueViewsetPermission(permissions.BasePermission):
    # surcharge la methode has_permission qui retourne toujours vrai
    def has_permission(self, request, view):
        #     si l'action = create on retourne vrai
        if view.action in ("destroy", "update"):
            return is_author(view.kwargs["project__pk"], request.user)
        try:
            is_contributor_found = is_contributor(
                view.kwargs["project__pk"], request.user)
        except KeyError:
            return True
        return is_contributor_found
class CommentViewsetPermission(permissions.BasePermission):
    # surcharge la methode has_permission qui retourne toujours vrai
    def has_permission(self, request, view):
        #     si l'action = create on retourne vrai
        # si action
        if view.action in ("destroy", "update"):
            return is_author_comment(view.kwargs["pk"], request.user)
        try:
            return is_author(
                view.kwargs["project__pk"], request.user
            ) or is_contributor(view.kwargs["project__pk"], request.user)
        except KeyError:
            return False
    
    