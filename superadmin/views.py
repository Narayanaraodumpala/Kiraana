from django.shortcuts import render
from django.views.generic import View
from superadmin.models import SuperAdmin
from app1.models import UserData
from product.models import Category,Brands
# Create your views here.


def superadmin(request):
    return render(request,'superadmin/admin.html')



        
def superadmin_register(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        
        super=SuperAdmin.objects.filter(email=email)
        if not super:
            SuperAdmin.objects.create(name=name,email=email,password=password)
            return render(request,'superadmin/admin.html',
                          {'msg':'Registration Successfull, Please Login'})
        else:
            return render(request,'superadmin/admin.html',
                          {'error':'This Account is Already registered, Please registered with Different Email or Just Login Instead Off'})
    else:
        return render(request,'superadmin/admin.html')
   
        
def superadmin_login(request):
    if request.method == 'POST':
        
        email=request.POST['email']
        password=request.POST['password']
        suser=SuperAdmin.objects.filter(email=email,password=password)
        if suser:
            users_count=UserData.objects.all().count()
            users=UserData.objects.all()
            category=Category.objects.all()
            brand=Brands.objects.all()
            totalcategory=Category.objects.all().count()
            totalbrand=Brands.objects.all().count()
            return render(request,'superadmin/index.html',{'user_count':users_count,'users':users,'category':category,
                                                           'brand':brand,'totalcategory':totalcategory,'totalbrand':totalbrand})
        else:
            return render(request,'superadmin/admin.html',{'error_msg':'Either Email or Password is Wrong'})
    else:
        return render(request,'superadmin/admin.html')
    
def superadmin_logout(request):
    return render(request,'superadmin/admin.html')

def add_category(request):
    return render(request,'superadmin/addcategory.html')
        
        
def users(request):
    user=UserData.objects.all().order_by('id')
    return render(request,'superadmin/allusers.html',{'users':user})