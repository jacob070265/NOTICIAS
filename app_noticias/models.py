from django.db import models
from datetime import datetime
from django.utils import timezone

class Temas(models.Model):
    titulo_tema=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.titulo_tema}"
class Noticias(models.Model):
    tema=models.ForeignKey(Temas,on_delete=models.CASCADE)
    titulo= models.CharField(max_length=100)
    descripcion = models.TextField()
    pub_date= models.DateTimeField("publicado") #models.fields.DateField(default=None,null=True,blank=True)
    foto1 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto2 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto3 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto4 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    foto5 = models.ImageField(upload_to="noticias/media",blank=True,null= True)
    votos=models.IntegerField(default=0)
    def __str__(self):
        return f"{self.titulo}-{self.descripcion}" 
     
    def publicados_recientemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


