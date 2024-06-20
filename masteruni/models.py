from django.db import models

# Create your models here.

class Usuario(models.Model):
    n_usuario     = models.CharField(max_length=20)
    contrasena  = models.CharField(max_length=15)
    def __str__(self):
        return str(self.n_usuario)
    
class Categoria(models.Model):
    id_categoria = models.IntegerField(db_column='idCategoria', primary_key=True)
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return str(self.nombre)

class Inventario(models.Model):
    id_prod = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=50)
    fecha_venc = models.DateField()
    stock = models.IntegerField()
    id_categoria = models.ForeignKey('Categoria',on_delete=models.CASCADE, db_column='idCategoria', null=True)

    def __str__(self):
        return str(self.id_prod, self.nombre_prod, self.fecha_venc, self.stock, self.id_categoria)