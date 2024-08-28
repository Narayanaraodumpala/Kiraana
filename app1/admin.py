from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from app1.resources import UserDataResource,UserResource
from app1.models import UserData
from django.contrib.auth.models import User

# Register your models here.
class UserDataAdmin(ImportExportModelAdmin):
    resource_class = UserDataResource 
    list_display = ["user", "unique_user_id", "forgot_password_token"]
    
admin.site.register(UserData, UserDataAdmin)

class UsersAdmin(ImportExportModelAdmin):
    resource_class = UserResource 
    list_display = ["username", "first_name", "email","last_name","last_login","is_active"]
  
admin.site.unregister(User)   
admin.site.register(User,UsersAdmin)

