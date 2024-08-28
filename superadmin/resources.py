from import_export import resources
from superadmin.models import SuperAdmin



class SuperAdminResource(resources.ModelResource):

    class Meta:
        model = SuperAdmin
        
