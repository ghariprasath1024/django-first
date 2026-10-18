from django.shortcuts import render,redirect
from .form import *
from .models import *


# Create your views here.
def index(request):
    return render(request,"index.html")

def apply_list(request):
    content={
        "test1":Test1.objects.all(),
        "test2":Test2.objects.all(),
        "test3":Test3.objects.all(),
        "test4":Test4.objects.all(),
        "test5":Test5.objects.all(),
    }
    return render(request,"apply.html",content)

def event_list(request):
    return render(request,"eventlist.html")

def test1(request):
    text={
        "form":test1form()
    }
    if request.method=="POST":
        form=test1form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"test1.html",text)

def test2(request):
    text={
        "form":test2form()
    }
    if request.method=="POST":
        form=test2form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"test2.html",text)    

def test3(request):
    text={
        "form":test3form()
    }
    if request.method=="POST":
        form=test3form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"test3.html",text) 

def test4(request):
    text={
        "form":test4form()
    }
    if request.method=="POST":
        form=test4form(request.POST)
        if form.is_valid():
            form.save()

    return render(request,"test4.html",text)

def test5(request):
    text={
        "form":test5form()
    }
    if request.method=="POST":
        form=test5form(request.POST)
        if form.is_valid():
            form.save()
    return render(request,"test5.html",text)  

def delete(request,id):
    test1=Test1.objects.get(id=id)
    test1.delete()
    
    return redirect("/backend/apply_list/")

def delete2(request,id):
    test2=Test2.objects.get(id=id)
    test2.delete()
    
    return redirect("/backend/apply_list/")


def delete3(request,id):
    test3=Test3.objects.get(id=id)
    test3.delete()
    
    return redirect("/backend/apply_list/")


def delete4(request,id):
    test4=Test4.objects.get(id=id)
    test4.delete()
    
    return redirect("/backend/apply_list/")


def delete5(request,id):
    test5=Test5.objects.get(id=id)
    test5.delete()
    
    return redirect("/backend/apply_list/")


def update1(request,id):
    test1=Test1.objects.get(id=id)
    const ={
        "form":test1form(instance=test1)
    }
    if request.method=="POST":
        test1tk=test1form(request.POST,instance=test1)
        if test1tk.is_valid():
            test1tk.save()
            return redirect('/backend/apply_list/')
                
    return render(request,"test1.html",const)


def update2(request,id):
    test2=Test2.objects.get(id=id)
    text={
        "form":test2form(instance=test2)
    }
    if request.method=="POST":
        form=test2form(request.POST,instance=test2)
        if form.is_valid():
            form.save()
            return redirect('/backend/apply_list/')
        
    return render(request,"test2.html",text) 

def update3(request,id):
    test3=Test3.objects.get(id=id)
    text={
        "form":test3form(instance=test3)
    }
    if request.method=="POST":
        form=test3form(request.POST,instance=text)
        if form.is_valid():
            form.save()
            return redirect("/backend/apply_list/")
    return render(request,"test3.html",text) 