from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name ='imagen' ,upload_to='projects')
    link = models.URLField(verbose_name = 'Direccion web', null = True, blank = True)
    created = models.DateTimeField(auto_now_add = True, verbose_name ='fecha de carga')
    updated = models.DateTimeField(auto_now = True, verbose_name ='fecha de modificacion')
       
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ["-created"]
   
    def __str__(self):
         return self.title   
   