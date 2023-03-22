from django.shortcuts import render, get_object_or_404
from galeria.models import Fotografia

def index(request):
    #fotografias = Fotografia.objects.all()
    fotografias = Fotografia.objects.order_by("-criado_em").filter(publicado=True)
    return render(request, 'galeria/index.html', {"fotografias": fotografias})

def imagem(request, foto_id):
    foto = get_object_or_404(Fotografia, pk=foto_id)
    return render(request, 'galeria/imagem.html', {"fotografia": foto})

def buscar(request):
    fotografias = Fotografia.objects.order_by("-criado_em").filter(publicado=True)
    if "campo_busca" in request.GET:
        campo_busca = request.GET['campo_busca'] 
        if campo_busca:
            fotografias = fotografias.filter(nome__icontains=campo_busca)

    return render(request, "galeria/index.html", {"fotografias": fotografias})