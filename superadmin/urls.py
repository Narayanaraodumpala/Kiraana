
from django.urls import path
from superadmin import views
from django.views.generic import TemplateView

urlpatterns = [

 path('superadmin/',views.superadmin,name='superadmin'),
 path('superadmin_register/',views.superadmin_register,name='superadmin_register'),
 path('superadmin_login/',views.superadmin_login,name='superadmin_login'),
 path('superadmin_logout/',views.superadmin_logout,name='superadmin_logout'),
 path('add_category/',views.add_category,name='add_category'),
 path('users/',views.users,name='users')

]