from django.shortcuts import render, redirect
from .models import Feedback, Admin
import random
import string
from django.core.mail import send_mail

# Create your views here.
def index(request):
    feedback=Feedback.objects.all()
    return render(request,'index.html',{'feedback':feedback})

def admin_login(request):
    otp=''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    email="microsoft.azure.anmol@gmail.com"
    member=Admin.objects.get(username=email)
    member.password=otp
    member.save()
    subject="Otp Verification"
    message="Here is your otp: "+str(otp)
    send_mail(subject,message,'microsoft.azure.anmol@gmail.com',[email],fail_silently=False)
    return render(request,'admin_login.html')

def adminlogin(request):
    otp=request.POST['input_usernamebox']
    if Admin.objects.filter(password=otp).exists():
        member=Admin.objects.get(password=otp)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        request.session['private_subha_key']=key
        member.private_key=key
        member.save()
        return redirect('admin_login_verified/'+key)

def admin_login_verified(request,member):
    member1=Admin.objects.get(private_key=member)
    if member1.private_key==request.session['private_subha_key']:
        return render(request,'admin.html',{'member':member1})

def blog_page(request):
    return render(request,'blog.html')

def contact_us(request):
    return render(request,'contact.html')