from import_export.admin import ImportExportModelAdmin
from django.contrib import admin 
from superadmin.resources import SuperAdminResource
from superadmin.models import SuperAdmin
# Register your models here.
class SuperAdminAdmin(ImportExportModelAdmin):
    resource_class = SuperAdminResource 
    list_display = ["name", "email", "password"]
    
admin.site.register(SuperAdmin, SuperAdminAdmin)

