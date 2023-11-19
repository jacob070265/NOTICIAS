from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='Home'),
    path('<int:id>/',views.detalle_noticia,name='Detalle'),
    path('encuesta/',views.encuesta,name='Encuesta'),
    path('img/',views.img,name='IMG'),
    path('votos/',views.votos,name='Votos'),
    path('temas/<int:id>',views.temas,name='Temas'),

]