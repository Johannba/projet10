from projects import models
from rest_framework import permissions
from django.core.exceptions import ObjectDoesNotExist 


# verifie si on est autheur ou pas projet      
def is_author(pk, user):
      # verifie si projet existe
      try:
            content = models.Project.objects.get(pk=pk)
      except ObjectDoesNotExist:
            # si existe pas exption qui retourne faux
            return False
      # si vrai on fait apparaitre l'autheur_user_id
      return content.author_user_id == user
      
def is_contributor(pk, user):
      try:
            models.Contributor.objects.get(user_id=user, project_id=pk)
      except ObjectDoesNotExist:
            return False
      return True  


class IsContributorOrAuthorProjectInProjectView(permissions.BasePermission):
    def has_permission(self, request, view):
      if view.action == "create":
            return True
      if view.action in ( "destroy", "update"):
            print(view.kwargs)
            return is_author(view.kwargs["pk"], request.user)
      

            