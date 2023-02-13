from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from new_app.forms import studentregister, Login_form, adminregister, MarkForm
from new_app.models import Mark, Student


# Create your views here.
def index(request):
    return render(request,"index.html")

def dashboard(request):
    return render(request,"dashboard.html")

def loginpage(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        password = request.POST.get("pass")
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_adm:
                return redirect("base")
            if user.is_student:
                return redirect("studentbase")
        else :
            messages.info(request,"Invalid credentials")

    return render(request,"login.html")



def base(request):
    return render(request,"admin12/base.html")


def adm_registration(request):
    form1=Login_form()
    print(form1)
    form2=adminregister()
    if request.method == "POST":
        form1 = Login_form(request.POST)
        form2 = adminregister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
               a = form1.save(commit=False)
               a.is_adm = True
               a.save()
               user1 = form2.save(commit=False)
               user1.user = a
               user1.save()
               return redirect('loginpage')

    return render(request,"admin12/adminregisterform.html",{'form1': form1,'form2': form2})



def add_mark(request):
    form = MarkForm()
    if request.method =='POST':
        form = MarkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("view_mark")
    return render(request,'admin12/add_mark.html',{'form':form})

def view_mark(request):
    data = Mark.objects.all()
    print(data)
    return render(request,'admin12/view_mark.html',{'data': data})



def edit_mark(request,id):
    a = Mark.objects.get(id=id)
    form =MarkForm(instance=a)
    if request.method == 'POST':
        form =MarkForm(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('view_mark')

    return render(request,'admin12/edit_mark.html',{'form':form})

def adminstudents_data(request):
    data=Student.objects.all
    print(data)
    return render(request,"admin12/adminview_studentdata.html",{"data": data})











def studentbase(request):
    return render(request,"student/studentbase.html")

def students(request):
    return render(request,"student/students.html")



def student_registration(request):
    form1=Login_form()
    print(form1)
    form2=studentregister()
    if request.method == "POST":
        form1 = Login_form(request.POST)
        form2 = studentregister(request.POST,request.FILES)

        if form1.is_valid() and form2.is_valid():
               a = form1.save(commit=False)
               a.is_student = True
               a.save()
               user1 = form2.save(commit=False)
               user1.user = a
               user1.save()
               return redirect('loginpage')

    return render(request,"student/students.html",{'form1': form1,'form2': form2})



def students_data(request):
    data=Student.objects.all
    print(data)
    return render(request,"student/students_data.html",{"data": data})



def delete_student(request,id):
 wm=Student.objects.get(id=id)
 wm.delete()
 return redirect("students_data")

#this is to delete workers data



def update_student(request,id):
    a = Student.objects.get(id=id)
    form = studentregister(instance=a)
    if request.method == 'POST':
        form = studentregister(request.POST,instance=a)
        if form.is_valid():
            form.save()
            return redirect('students_data')

    return render(request,'student/update_student.html',{'form':form})



