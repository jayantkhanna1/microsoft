from django.shortcuts import render, redirect
from .models import Feedback, Admin
import random
import string

# Create your views here.
def index(request):
    feedback=Feedback.objects.all()
    return render(request,'index.html',{'feedback':feedback})

def admin_login(request):
    return render(request,'admin_login.html')

def adminlogin(request):
    user=request.POST['input_usernamebox']
    pwd=request.POST['input_passwordbox']
    if Admin.objects.filter(username=user,password=pwd).exists():
        member=Admin.objects.get(username=user,password=pwd)
        key=''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(20))
        request.session['private_subha_key']=key
        member.private_key=key
        member.save()
        return redirect('admin_login_verified/'+key)

def admin_login_verified(request,member):
    member1=Admin.objects.get(private_key=member)
    if member1.private_key==request.session['private_subha_key']:
        return render(request,'admin.html',{'member':member1})
