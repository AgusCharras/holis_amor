from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Mes, Dia
import datetime

@receiver(post_save, sender=Mes)
def crear_dias_mes(sender, instance, created, **kwargs):
    if created:  # Si el mes es creado por primera vez
        for numero_dia in range(1, instance.dias + 1):  # Instanciar días
            Dia.objects.create(
                mes=instance,
                numero=numero_dia,
            )
