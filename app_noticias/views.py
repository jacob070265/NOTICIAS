from django.shortcuts import render,HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import Noticias,Temas

def home(request):
    noticias = Noticias.objects.all()
    ultima_noticia=Noticias.objects.order_by('-pub_date')[:1]
    temas=Temas.objects.all()
    return render(request,'home.html', {'noticias': noticias, 'ultima':ultima_noticia, 'temas':temas})

def detalle_noticia (request,id):
    noticia=get_object_or_404(Noticias,pk=id)
    return render (request,'base.html', {'noticia': noticia})

def encuesta (request):
    noticias = Noticias.objects.all()
    return render (request,'encuesta.html', {'noticias': noticias})


def votos (request):
    noticias = Noticias.objects.all()
    try:
        noticia = Noticias.objects.get(titulo = request.POST['choice']) 
    except:
        return render(request, 'detalles.html',{'error_message': 'error insertando votos', 'noticias': noticias})

    else:
        noticia.votos+=1
        noticia.save()
        return render(request,'detalles.html', {'noticias': noticias,})
        #return HttpResponseRedirect('detalles.html') 
        

def temas (request, id):
    tema=Temas.objects.get(id = id)
    noticias_del_tema=Noticias.objects.filter(tema=id)
    return render(request,'temas.html', {'tema': tema, 'noticias_del_tema':noticias_del_tema})


def img(request):
    noticias = Noticias.objects.all()
    ultima_noticia=Noticias.objects.order_by('-pub_date')[:1]
    temas=Temas.objects.all()
    if request.POST.get('tema', False):
        noticia=Noticias(tema=request.POST['tema'], titulo=request.POST['titulo'],descripcion=request.POST['descripcion'],pub_date=timezone.now(), foto1=request.POST['img'])
        noticia.save()
        return render(request,'home.html', {'mensaje': 'noticia guardada.','temas':temas,'noticias':noticias, 'ultima_noticia':ultima_noticia})
    else:
        return render(request,'home.html', {'mensaje': "Faltan campos por rellenar",'temas':temas, 'noticias':noticias, 'ultima_noticia':ultima_noticia})
            
        


