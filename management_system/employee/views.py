
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
#from employee.views import home
from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_required(login_url='login')
def login_view(request):
    if request.method=="POST":
        l_name = request.POST.get('l_name')
        l_pass = request.POST.get('l_pass')
        authon = authenticate(request,username=l_name,password=l_pass)
        
        if authon is not None:
            login(request,authon)
            return redirect('home')
        else:
            return render(request,'login.html')
            #return HttpResponse("<h1>user or passward not match!!!!</h1>")
        
    return render(request,'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



def register_view(request):
    if request.method=='POST':
        uname=request.POST.get('u_name')
        uemail =request.POST.get('email')
        upass = request.POST.get('pass')
        my_user = User.objects.create_user(uname,uemail,upass)
        my_user.save()
        return redirect('login')
   

    return render(request,'register.html')


from django.shortcuts import render,redirect
from . models import Employe

# Create your views here.
def home(request):
    fetch_emp=Employe.objects.all()
    return render(request,'home.html',{"fetch_emp":fetch_emp})

def add_employ(request):
    if request.method == 'POST':
        print('added')
        e_id = request.POST.get('e_id')
        e_name = request.POST.get('e_name')
        e_email = request.POST.get('e_email')
        e_bdate = request.POST.get('e_bdate')
        e_gender = request.POST.get('e_gender')
        e_address = request.POST.get('e_address')
        e_position = request.POST.get('e_position')
        e_salary = request.POST.get('e_salary')
        e_phone = request.POST.get('e_phone')

        e = Employe()
        e.Empid = e_id
        e.Name = e_name
        e.Email = e_email
        e.Birthdate = e_bdate
        e.Gender = e_gender
        e.Adress = e_address
        e.Position = e_position
        e.Salary = e_salary
        e.Phone =e_phone

        e.save()
        return render(request,'login.html')
    return render(request,'add.html')

def delete_(request,Empid):
    e = Employe.objects.get(pk=Empid)
    e.delete()
    return redirect(home)

def update_(request,Empid):
    emp=Employe.objects.get(pk=Empid)
    return render(request,'update.html',{'emp':emp})

def do_update_(request,Empid):
    e_id = request.POST.get('e_id')
    e_name = request.POST.get('e_name')
    e_email = request.POST.get('e_email')
    e_bdate = request.POST.get('e_bdate')
    e_gender = request.POST.get('e_gender')
    e_address = request.POST.get('e_address')
    e_position = request.POST.get('e_position')
    e_salary = request.POST.get('e_salary')
    e_phone = request.POST.get('e_phone')

    e=Employe.objects.get(pk=Empid)

    e.Empid = e_id
    e.Name = e_name
    e.Email = e_email
    e.Birthdate = e_bdate
    e.Gender = e_gender
    e.Adress = e_address
    e.Position = e_position
    e.Salary = e_salary
    e.Phone =e_phone

    e.save()

    return redirect(home)

