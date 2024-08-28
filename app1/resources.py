from import_export import resources
from app1.models import UserData
from django.contrib.auth.models import User


class UserDataResource(resources.ModelResource):

    class Meta:
        model = UserData
        
class UserResource(resources.ModelResource):

    class Meta:
        model = User