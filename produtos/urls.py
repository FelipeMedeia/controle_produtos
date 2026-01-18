from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('relatorio-estoque/', views.relatorio_estoque, name='relatorio_estoque'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
