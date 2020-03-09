from django.shortcuts import render, redirect
from musica.forms import LoginForm
from django.contrib.auth import authenticate,login,logout


def login_page (request):
    message = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username= request.POST["username"]
            password= request.POST["password"]
            user= authenticate (username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("home")
                else:
                    message = "tu usuario esta inactivo"
            else:
                message= "te equivocaste en escribir alguna wea imbecil de mierda"
    else:
        form = LoginForm()
    return render(request,"login/login.html", {"message": message, "form": form})

def home(request):
    return render(request,"home/home.html")

def salir(request):
    logout(request)
    return redirect("home")