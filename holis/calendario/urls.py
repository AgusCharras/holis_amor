from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.lista_meses, name='lista_meses'),
    path('mes/<int:mes_id>/', views.detalle_mes, name='detalle_mes'),
    path('dia/<int:dia_id>/', views.detalle_dia, name='detalle_dia'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
