from django.shortcuts import render,redirect
from .models import Forms

# Create your views here.

def index(request):
    aravinth="FUll stack devop"
    return render(request, "index.html",{'aravinth':aravinth})


def testing(request):
    return render(request, "testing.html")

def flex(request):
    return render(request, "flex.html")

def sample(request):
    return render(request, "sample.html")

def form(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        Forms.objects.create(name = name,age = age ,dob = dob)
    return render(request, "form.html")


def form_result(request):
    result=Forms.objects.all()
    return render(request,'form_result.html',{"result":result})


def form_edit(request,id):
    edit = Forms.objects.filter(id=id)
    if request.method == 'POST':
        name= request.POST.get('name')
        age = request.POST.get('age')
        dob = request.POST.get('dob')
        Forms.objects.filter(id=id).update(name = name,age = age ,dob = dob)

    return render(request,'form_edit.html',{"edit":edit})


def form_delete(request, id):
    delete = Forms.objects.filter(id=id)  
    delete.delete()                            
    return redirect("form_result")