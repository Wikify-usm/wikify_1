from django.conf.urls import url, include
from apps.usuario.view import RegistroUsuario
from apps.usuario.views import index


urlpatterns = [
    url(r"^registrar/",RegistroUsuario.as_view(),name="registrar"),
]
