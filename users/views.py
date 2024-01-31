from django.shortcuts import render,redirect
from .form import *
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def register(request):
    form=UserForm()
    context={
        "form":form
    }
    if request.method=="POST":
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    return render(request,'register.html',context)
def userLogin(request):
    if request.method=="POST":
        userName=request.POST["userName"]
        userPass=request.POST["userPass"]
        user = authenticate(request,username=userName,password=userPass)
        if user is not None:
            login(request,user)
            return redirect("browse")
        else:
            return render(request,"login.html")
    return render(request,"login.html")
def profiles(request):
    profiller=Profiles.objects.filter(owner=request.user)
    context={
        "profiller":profiller
    }
    return render(request,"browse.html",context)
def createProfile(request):
    form=ProfileForm()
    if request.method=="POST":
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile=form.save(commit=False)
            profile.owner=request.user
            profile.save()
            return redirect("browse")
    context={
        "form":form
    }
    return render(request,"create-profile.html",context)

def userLogout(request):
    logout(request)
    return redirect("index")

def userAccount(request):
    profil=request.user
    context={
        "profil":profil
    }
    return render(request,"hesap.html",context)
def userDelete(request):
    profil=request.user
    profil.delete()
    return redirect("index")