from django.contrib import admin
from django.urls import path
from app1 import views
from django.views.generic import TemplateView

from E_kiraana import settings
from django.templatetags.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index,name='home'),
   
    path('superadminview/',views.superadminview,name='superadminview'),
    path('signup', views.Rigester.as_view(), name="signup"),
    
     path('logout/',views.user_logout,name='logout'),
    path('signin', views.Signin.as_view(), name="signin"),
    path('email-verify/',views.VerifyEmail.as_view(),name='email-verify'),
    path('forgot_request/',views.request_reset,name='forgot_request'),
   #path('change_password/<token>',views.change_password,name='change_password'),
   path('user_dashboard/',TemplateView.as_view(template_name="user/Dashboard/dashboard.html"),name='user_dashboard'),
   path('profile/',views.profile,name='profile'),
   path('export_list/',views.export_list,name='export_list'),
    path('export_pdf/',views.export_pdf,name='export_pdf'),
    path('import_excel/',views.import_excel,name='import_excel'),
    path('import_excel_file/',views.import_excel_file,name='import_excel_file'),
    


]

