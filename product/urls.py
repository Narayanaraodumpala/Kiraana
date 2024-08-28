
from django.urls import path
from E_kiraana import settings
from django.conf.urls.static import static
from product import views


urlpatterns = [
path('savecategory/', views.Savecategory.as_view(),name='savecategory'),
path('display_categories/',views.Display_categories.as_view(),name='display_categories'),
path('editcategory/<int:pk>',views.Editcategory.as_view(),name='editcategory'),
 path('deletecategory/<int:pk>',views.deletecategory,name='deletecategory'),
 path('deletecategorydone/<int:pk>',views.deletecategorydone,name='deletecategorydone'),
 path('addbrand/',views.Addbrand.as_view(),name='addbrand'),
 path('brandlist/',views.BrandList.as_view(),name='brandlist'),
 path('editbrand/<int:pk>',views.Editbrand.as_view(),name='editbrand'),
 path('deletebrand/<int:pk>',views.deletebrand,name='deletebrand'),
 path('deletebranddone/<int:pk>',views.deletebranddone,name='deletebranddone'),
 path('categoryexport_pdf/',views.categoryexport_pdf,name='categoryexport_pdf'),
 path('categoryexport_excel/',views.categoryexport_excel,name='categoryexport_excel'),
 path('brandexport_pdf/',views.brandexport_pdf,name='brandexport_pdf'),
 path('brandexport_excel/',views.brandexport_excel,name='brandexport_excel')
 


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)