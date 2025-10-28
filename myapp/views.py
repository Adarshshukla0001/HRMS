from django.shortcuts import render,redirect,reverse
from . models import ad
from adminzone.models import Employee
from django.core.exceptions import ObjectDoesNotExist
from . smssender import sendsms
# Create your views here.
def index(request):
    return render(request,'index.html')
def adlogin(request):
    return render(request,'adlogin.html')
def emplogin(request):
    return render(request,'emplogin.html')

def validateuser(request):
        name=request.POST['aid']
        password=request.POST['apass']
        msg=''
        try:
            obj=ad.objects.get(name=name,password=password)
            if obj is not None:
                request.session['userid']=name
                return redirect(reverse('adminzone:index'))
        except ObjectDoesNotExist:
            msg='Invalid User'
        return render(request,"adlogin.html",{'msg':msg})
def validateemp(request):
        name=request.POST['aid']
        password=request.POST['apass']
        msg=''
        try:
            obj=Employee.objects.get(empid=name,empname=password)
            if obj is not None:
                request.session['empid']=name
            return redirect(reverse('empzone:index'))
        except ObjectDoesNotExist:
            msg='Invalid User'
        return render(request,"emplogin.html",{'msg':msg})
def contact(request):
     if request.method=='POST':
          mobile=request.POST['mobile']
          sendsms(mobile)
          
     return render(request,"contact.html")
def logout(request):
        request.session['userid']=None
        return render(request,'index.html') 
def about(request):
    return render(request,'about.html')
def services(request):
    return render(request,'services.html')