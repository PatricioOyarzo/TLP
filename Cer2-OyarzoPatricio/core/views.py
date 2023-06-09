from urllib import request
from django.shortcuts import get_object_or_404, redirect, render
from .models import Comunicado
from .models import Categoria
from .formato import ComunicadoForm

# Create your views here.

def principal(request): #para obtener los comunicados y ordenarlos
    comunicados = Comunicado.objects.order_by('fecha_envio')
    niveles = Comunicado.Nivel_Choices
    categorias = Categoria.objects.all()

    filtrar_niveles = request.GET.get('nivel')
    filtrar_categoria = request.GET.get('categoria')

    if filtrar_categoria:
        comunicados = comunicados.filter(nivel = filtrar_niveles)

    if filtrar_niveles:
        comunicados = comunicados.filter(categoria_nombre = filtrar_categoria)
    
    return render(request, 'core/principal.html', {'comunicados': comunicados, 'niveles': niveles, 'categorias': categorias})


def comunicado_detalle(request):    # deglose del comunicado si no existe, error 404
    return render(request, 'core/comunicado.html')


def crear_comunicado(request):
    if request.method == 'Publicacion':
        formato = ComunicadoForm(request.POST)
        if  formato.is_valid():
            comunicado = formato.save(commit=False)
            comunicado.publicado_por = request.user
            comunicado.save()
            return redirect('principal')
    return render(request, 'core/crearcomunicado.html')


def editar_comunicado(request, comunicado_id):
    comunicado = get_object_or_404(Comunicado, pk=comunicado_id)
    if request.method == 'POST':
        format = ComunicadoForm(request.POST, instance=comunicado)

