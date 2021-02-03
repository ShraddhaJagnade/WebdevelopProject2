from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User
# Create your views here.

def first(request):
    return render(request, 'enroll/first.html')

def add_data(request):
    if request.method == 'POST':
        form = StudentRegistration(request.POST)
        if form.is_valid():
            nm = form.cleaned_data['Name']
            dept = form.cleaned_data['Department']
            add = form.cleaned_data['Address']
            cty = form.cleaned_data['City']
            em = form.cleaned_data['Email']
            pwd = form.cleaned_data['Password']
            reg = User(Name=nm, Department=dept, Address=add, City=cty, Email=em, Password=pwd ) 
            reg.save()
            form = StudentRegistration()

        else:
            form = StudentRegistration()
    else:
        form = StudentRegistration()

    return render(request, 'enroll/add.html', {'form':form})

def add_show(request):
    stud = User.objects.all()
    return render(request, 'enroll/addnshow.html', {'stu':stud})

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        form = StudentRegistration(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        else:
            pi = User.objects.get(pk=id)
            form = StudentRegistration(instance=pi)
    else:
        form = StudentRegistration()

    return render(request, 'enroll/update.html', {'form':form})        

def delete_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')

