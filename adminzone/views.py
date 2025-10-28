from django.shortcuts import render,redirect,reverse
from . models import Employee, Nfc,Attend,Salary
from empzone.models import Feed,Leave
import datetime



# Create your views here.
def index(request):
    if request.session['userid']:
        e=Employee.objects.all()
        f=Feed.objects.all()
        g=Leave.objects.all()
        return render(request,'home.html',{'e':e,'f':f,'g':g}) 
    return render(request,'index.html') 
  
def addemp(request):
    if request.method=='POST':
        id=request.POST['empid']
        name=request.POST['empname']
        dept=request.POST['department']
        sal=request.POST['salary']
        emp=Employee(empid=id,empname=name,department=dept,salary=sal,mobile=0,email='---',address='---',gender='---',qua='---',exp='---')
        emp.save()
    return render(request,'addemp.html')
def viewemp(request):
    emp=Employee.objects.all()
    return render(request,'viewemp.html',{'emp':emp})
def nfc(request):
    if request.method=='POST':
        nfcid = request.POST['nfcid']
        nfc = request.POST['nfc']
        nfcs=Nfc(nfcid=nfcid,nfc=nfc)
        nfcs.save()
    n=Nfc.objects.all()    
    return render(request,'nfc.html',{'n':n})
def feed(request):
    f=Feed.objects.all()
    return render(request,'feed.html',{'f':f})
def attend(request):
    e=Employee.objects.all()
    return render(request,'attend.html',{'e':e})
def viewattend(request):
    a=Attend.objects.all()
    return render(request,'viewattend.html',{'a':a})
def sal(request):
    e=Employee.objects.all()
    return render(request,'sal.html',{'e':e})
def sendsal(request):
    e=Salary.objects.all()
    return render(request,'sendsal.html',{'e':e})
    
def leave(request):
    l=Leave.objects.all()
    return render(request,'leave.html',{'l':l})
def deleteemp(request,empid):
    emp=Employee.objects.get(empid=empid)
    emp.delete()
    return redirect(reverse('adminzone:viewemp'))
def accept(request,empid):
     l=Leave.objects.get(empid=empid)
     l.status=0
     l.save()
     return redirect(reverse('adminzone:leave'))
def reject(request,empid):
     l=Leave.objects.get(empid=empid)
     l.status=1
     l.save()
     return redirect(reverse('adminzone:leave'))
def send(request,empid):
     l=Salary.objects.get(empid=empid)
     l.status=0
     l.save()
     return redirect(reverse('adminzone:sendsal'))
def present(request,empid):
    e=Employee.objects.get(empid=empid)
    id=e.empid
    name=e.empname
    dept=e.department
    curr=datetime.datetime.today()
    status=1
    a=Attend(empid=empid,empname=name,department=dept,date=curr,status=status)
    a.save()
    return redirect(reverse('adminzone:attend'))
def addsal(request,empid):
    e=Employee.objects.get(empid=empid)
    id=e.empid
    name=e.empname
    dept=e.department
    curr=datetime.datetime.today()
    sal=e.salary
    status=1
    s=Salary(empid=id,empname=name,department=dept,salary=sal,date=curr,status=status)
    s.save()
    return redirect(reverse('adminzone:sendsal'))
def ab(request,empid):
     a=Attend.objects.get(empid=empid)
     a.status=1
     a.save()
     return redirect(reverse('adminzone:viewattend'))
def pr(request,empid):
     a=Attend.objects.get(empid=empid)
     a.status=0
     a.save()
     return redirect(reverse('adminzone:viewattend'))
