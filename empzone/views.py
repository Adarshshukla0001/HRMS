from django.shortcuts import render,redirect,reverse
from adminzone.models import Employee,Nfc,Salary
from . models import Feed,Leave
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def index(request):
    if request.session['empid']:
        a=request.session['empid']
        emp=Employee.objects.get(empid=a)
        return render(request,'empindex.html',{'emp':emp})
    
def nfc(request):
        x=Nfc.objects.all()
        return render(request,'empnfc.html',{'x':x})
def empfeed(request):
    if request.method=='POST':
        id=request.POST['empid']
        name=request.POST['empname']
        dept=request.POST['department']
        feedtype=request.POST['feed']
        msg=request.POST['msg']
        f=Feed(empid=id,empname=name,department=dept,feedtype=feedtype,msg=msg)
        f.save()
    return render(request,'empfeed.html')
def empleave(request):
    if request.method=='POST':
        id=request.POST['empid']
        name=request.POST['empname']
        dept=request.POST['department']
        sub=request.POST['subject']
        fr=request.POST['fr']
        to=request.POST['to']
        msg=request.POST['msg']
        l=Leave(empid=id,empname=name,department=dept,subject=sub,fr=fr,to=to,status=0,msg=msg)
        l.save()
    a=request.session.get('empid')
    try:
       l=Leave.objects.get(empid=a)
    except Leave.DoesNotExist:
        l = None   
    return render(request,'empleave.html',{'l':l})
def empsal(request):
    if request.session['empid']:
       a=request.session['empid'] 
       s=Salary.objects.get(empid=a)
       return render(request,'empsal.html',{'s':s})
def updateemp(request):
    if request.session['empid']:
        if request.method=='POST':
            id=request.POST['empid']
            mobile=request.POST['mobile']
            email=request.POST['email']
            gender=request.POST['gender']
            qua=request.POST['qua']
            exp=request.POST['exp']
            address=request.POST['address']
            e=Employee.objects.get(empid=id)
            e.mobile=mobile
            e.email=email
            e.gender=gender
            e.qua=qua
            e.exp=exp
            e.address=address
            e.save()
            return redirect(reverse('empzone:index'))
        a=request.session['empid']
        e=Employee.objects.get(empid=a)
        return render(request,'updateemp.html',{'e':e})
def logout(request):
        request.session['userid']=None
        return render(request,'index.html')     