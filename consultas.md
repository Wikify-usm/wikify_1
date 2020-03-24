# wikify_1
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Cancion
class BuscarView(TemplateView):
    template_name='subirCanciones/buscar.html'
    

    def post(self, request,*args, **kwargs):
        buscar=request.POST['buscalo']
        tema=Cancion.objects.filter(nombre__contains=buscar)
        artis=Cancion.objects.filter(artista__contains=buscar)
        genr=Cancion.objects.filter(genero__contains=buscar)
        albu=Cancion.objects.filter(album__contains=buscar)
        
        if tema:
            ahora=tema.all()
        elif artis:
            ahora=artis.all()
        elif genr:
            ahora=genr.all()
        elif albu:
            ahora=albu.all()
        else:
            ahora='no esta disponible'
        

        contexto={'ahora': ahora}
        
    
