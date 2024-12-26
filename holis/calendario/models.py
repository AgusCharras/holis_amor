from django.db import models

# Create your models here.

class Mes(models.Model):
    nombre = models.CharField(max_length=20)
    dias = models.IntegerField()
    
    def __str__(self):
        return self.nombre
    
class Dia(models.Model):
    mes = models.ForeignKey(Mes, related_name="dias_mes", on_delete=models.CASCADE)
    numero = models.IntegerField()
    imagen = models.ImageField(upload_to='dias_imagenes/', null=True, blank=True)
    texto = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f"dia {self.numero} de {self.mes.nombre}"
    
    @property
    def tiene_imagen(self):
        return bool(self.imagen)
    
    