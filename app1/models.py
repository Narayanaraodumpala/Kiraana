from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserData(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    
    unique_user_id=models.CharField(max_length=10,null=True)
    forgot_password_token=models.CharField(max_length=100,null=True)

    class Meta:
        db_table='Users'

    def __str__(self):
        return self.user.username
    
    
# class Login_Logout(models.Model):
#     user=models.ForeignKey(User,related_name='login_logout_user',on_delete=models.CASCADE)
#     login_at=models.TimeField(null=True)
#     logout_at=models.TimeField(null=True)

#     class Meta:
#         db_table='Login_Logout_Sessions'

#     def __str__(self):
#         return str(self.login_at) + ' '+ str(self.login_at)