from django.contrib.auth import login, authenticate
from Apps.usuario.forms import Registroform
from django.shortcuts import render, redirect



def Registro_usuario(request):
    data = {
        'form': Registroform()
    }

    if request.method == "POST":
        formulario = Registroform(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='home')
    return render(request, 'registrar.html', data)

