from django.db import models

# Create your models here.
class Categorias(models.Model):
    descripcion = models.CharField(max_length=30)

    def __str__(self):
        return f"Descripcion {self.id}:\n{self.descripcion}"

#Tras crear un modelo se debe ejecutar 
# manage.py makemigrations -> despliega sobre la base de datos
# manage.py migrate -> implementa los cambios

# CONTROL DESDE LA CONSOLA
# manage.py shell -> consola de django
#   from JAGUARETE_APP import Categorias
# categoria = Categoria(descripcion="Una descripcion")
# categoria.save() //se guarda en la bd (esto coloca una id al ejemplar)