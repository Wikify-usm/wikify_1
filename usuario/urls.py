from django.conf.urls import url, include
from Apps.usuario.view import Registro_usuario
from Apps.usuario.views import index
from django.urls import path


urlpatterns = [

    path('registrar/',Registro_usuario,name='registrar'),

]
