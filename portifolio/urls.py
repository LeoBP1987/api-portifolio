from django.urls import path, include
from rest_framework import routers
from portifolio.views import UsuariosCustomizadosViewSet, TecnologiasViewSet, ProjetosViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuariosCustomizadosViewSet, basename='Usuarios')
router.register('tecnologias', TecnologiasViewSet, basename='Tecnologias')
router.register('projetos', ProjetosViewSet, basename='Projetos')

urlpatterns = [
    path('', include(router.urls))
]
