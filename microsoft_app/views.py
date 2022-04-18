from django.shortcuts import render, redirect
from .models import Admin, Training, Blogs, Chapter
import random
import string
import json
from django.contrib import messages
from django.core.mail import send_mail


def index(request):
    rand=[]
    for x in range(6):
        rand.append(random.randint(0, 11))
    return render(request,'index.html',{'feedback':json.loads(json.dumps(rand)),'trainings':Training.objects.all()})

def index_from_getintouch(request,training):
    return redirect('index')

def blog_from_getintouch(request,training):
    return redirect('blog')

def contact_from_getintouch(request,training):
    return redirect('contact_us')

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
        return render(request,'admin.html',{'admin':member1,'trainings':Training.objects.all(),'blogs':Blogs.objects.all(),'chapter':Chapter.objects.all()})

def blog_page(request):
    return render(request,'blog.html',{'blogs':Blogs.objects.all(),'chapter':Chapter.objects.all()})

def contact_us(request):
    return render(request,'contact.html')

def contact_send_mail(request):
    name=request.POST['name']
    user_email=request.POST['email']
    subject='User Feedback'
    message=request.POST['message']
    phone=request.POST['phone']
    final_message="Name: "+name+"\n Email: "+user_email+"\n Mobile number: "+phone+"\n message: "+message
    email="microsoft.azure.anmol@gmail.com"
    send_mail(subject,final_message,'microsoft.azure.anmol@gmail.com',[email],fail_silently=False)
    messages.info(request,'message sent!')
    return redirect('contact_us')

def get_training(request,training):
    return render(request,'get_training.html',{'training':training})
    
def get_training_send_mail(request,training):
    print("cool hai")
    name=request.POST['name']
    user_email=request.POST['email']
    subject="Would like to purchase "+training+" training"
    message=request.POST['message']
    phone=request.POST['phone']
    final_message="Name: "+name+"\n Email: "+user_email+"\n Mobile number: "+phone+"\n message: "+message +"\n Training: "+training
    email="microsoft.azure.anmol@gmail.com"
    send_mail(subject,final_message,'microsoft.azure.anmol@gmail.com',[email],fail_silently=False)
    messages.info(request,'message sent!')
    return redirect('index') 

def certificates(request):
    return render(request,'certificates.html')

def transcripts(request):
    return render(request,'transcripts.html')

def badges(request):
    return render(request,'badges.html')

def add_new_training(request):
    newt=request.POST['newtraining']
    Training.objects.create(training=newt)
    return redirect('admin_login_force')

def delete_training(request):
    newt=request.POST['training_name']
    Training.objects.get(training=newt).delete()
    return redirect('admin_login_force')

def admin_login_force(request):
    return render (request,'admin.html',{'admin':Admin.objects.all(),'trainings':Training.objects.all(),'blogs':Blogs.objects.all(),'chapter':Chapter.objects.all()})

def addnewchapter(request):
    blogs=Blogs.objects.all()
    highest=0
    for x in blogs:
        highest=x.chapter
    highest=str(int(highest)+1)
    Chapter.objects.create(chapter=highest)
    Blogs.objects.create(chapter=highest,page_number=str(highest)+".0",blog="")
    return redirect('admin_login_force')

def addnewpage(request):
    lastpage=request.POST['last_chapter']
    chapter=lastpage.split('.')
    pagenum=float(float(lastpage)+0.1)
    pagenum=str(round(pagenum, 2))
    blogs=Blogs.objects.create(chapter=chapter[0],page_number=pagenum,blog="")
    return redirect('admin_login_force')

def saveblog(request):
    pagenum=request.POST['pagenumber']
    blog=request.POST['blog']
    blog_obj=Blogs.objects.get(page_number=pagenum)
    blog_obj.blog=blog
    blog_obj.save()
    return redirect('admin_login_force')
