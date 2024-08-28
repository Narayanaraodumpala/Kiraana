from django.core.mail import send_mail
import uuid
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site


def send_forgot_password_mail(email,token,request):
    #token=str(uuid.uuid4())
    
    subject='your forgot passwoird link'
    current_site = get_current_site(request).domain
    #relativeLink = reverse('email-verify')
    absurl = 'http://' + current_site +'/change_password/'+   str(token)
    
    message= f'hi , click on the link to reset your password '+ absurl
    email_form= settings.EMAIL_HOST_USER
    reciepent_list=[email]
    send_mail(subject,message,email_form,reciepent_list)

    return True
    