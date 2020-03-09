from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from Apps.usuario.forms import Registroform
from django.shortcuts import render

class RegistroUsuario(CreateView):
    model = User
    template_name = 'usuario/registrar.html'
    form_class = Registroform
    success_url = reverse_lazy('admin')