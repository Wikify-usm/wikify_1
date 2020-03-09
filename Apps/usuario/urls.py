from django.conf.urls import url, include
from Apps.usuario.view import RegistroUsuario
from Apps.usuario.views import index


urlpatterns = [
    url(r'^registrar/',RegistroUsuario.as_view(),name='registrar'),
]
