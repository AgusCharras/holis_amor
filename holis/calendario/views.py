from django.shortcuts import render, get_object_or_404
from .models import Mes, Dia

def lista_meses(request):
    meses = Mes.objects.all()
    return render(request, 'lista_meses.html', {'meses': meses})

from calendar import monthrange
import datetime

def detalle_mes(request, mes_id):
    mes = get_object_or_404(Mes, id=mes_id)
    # Obtener todos los días asociados a este mes
    dias = mes.dias_mes.all()
    
    # Determinar el año y el mes actual para los cálculos del calendario (asumimos un año fijo para personalización)
    year = 2024  # Puedes personalizar este año o hacerlo dinámico
    mes_num = datetime.datetime.strptime(mes.nombre, "%B").month  # Convertir nombre del mes a número
    
    # Obtener el primer día de la semana y cuántos días tiene el mes
    first_weekday, total_days = monthrange(year, mes_num)
    
    # Crear una lista para representar semanas y días
    semanas = [[]]
    contador_dia = 1

    # Rellenar los días iniciales vacíos
    for _ in range(first_weekday):
        semanas[0].append(None)

    # Rellenar los días reales
    for dia in range(1, total_days + 1):
        if len(semanas[-1]) == 7:
            semanas.append([])  # Nueva semana
        semanas[-1].append(dias.filter(numero=dia).first())  # Agregar el objeto del día si existe
    
    # Rellenar los días finales vacíos (para completar la última fila)
    while len(semanas[-1]) < 7:
        semanas[-1].append(None)

    return render(request, 'detalle_mes.html', {'mes': mes, 'semanas': semanas})


def detalle_dia(request, dia_id):
    dia = get_object_or_404(Dia, id=dia_id)
    return render(request, 'detalle_dia.html', {'dia': dia})
