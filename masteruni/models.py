from django.db import models

# Create your models here.

class Usuario(models.Model):
    n_usuario     = models.CharField(max_length=20)
    contrasena  = models.CharField(max_length=15)
    def __str__(self):
        return str(self.n_usuario)
    
# class Categoria(models.Model):
#     id_categoria = models.IntegerField(db_column='idCategoria', primary_key=True)
#     nombre = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.nombre)

class Inventario(models.Model):
    id     = models.CharField(primary_key=True, max_length=5)
    nombre = models.CharField(max_length=30)
    categoria = models.CharField(max_length=30, default='categoria')
    stock  = models.IntegerField()
    fecha_venc = models.DateField()
    

