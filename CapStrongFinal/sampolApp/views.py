from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .forms import *
from .models import *

def home(request):
    return render(request, 'home.html')

class dashboardView(View):
    def get(self,request):
        return render(request, 'dashboard.html')
    def post(self, request):
        if request.method=='POST':
            if 'btnUpdate' in request.POST:
                print('update profile button clicked')
                sId=request.POST.get("r-studentId")
                sName=request.POST.get("r-sName")
                pNum=request.POST.get("r-pNum")
                idNum=request.POST.get("r-idNum")
                type=request.POST.get("r-vType")
                update_Register=Register.objects.filter(student_id=sId).update(sName=sName, plateNum=pNum, idNum=idNum, vType=type)
                print(update_Register)
                print('profile updated')
            elif 'btnDelete' in request.POST:
                printf('delete button clicked')
                studentId=request.POST.get("register-studentId")
                register=Register.objects.filter(student_id=studentId).delete()
                print('record deleted')

        return redirect('dashboardView')

class loginView(View):
    def get(self,request):
        return render(request, 'login.html')
    
    def post(self, request):
        form=UserForm(request.POST)
        fname=request.POST.get("fname")
        print(fname)
        lname=request.POST.get("lname")
        print(lname)
        email=request.POST.get("email")
        print(email)
        uname=request.POST.get("uname")
        print(uname)
        password=request.POST.get("pass")
        print(password)
        if form.is_valid():
            fname=request.POST.get("fname")
            lname=request.POST.get("lname")
            email=request.POST.get("email")
            uname=request.POST.get("uname")
            password=request.POST.get("pass")

        form=User(Fname=fname, Lname=lname, Email=email, Uname=uname, Pass=password)

        form.save()

        return redirect('login.html')

class indexView(View):
    def get(self,request):
        return render(request, 'index.html')

    def post(self, request):        
        form = RegistrationForm(request.POST)        
      
        if form.is_valid():
            # try:
            num = request.POST.get("idnum")
            name = request.POST.get("sName")
            plate = request.POST.get("plate")
            vType = request.POST.get("type")

        form = Registrations(sName = sName,idNum = num, plateNum = plateNum, vType = vType)
        
        form.save()
        return redirect('indexView')


