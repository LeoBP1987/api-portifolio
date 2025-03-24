from django.urls import path, include
from rest_framework import routers
from portifolio.views import UsuariosCustomizadosViewSet, TecnologiasViewSet, ProjetosViewSet, LoginViewSet

router = routers.DefaultRouter()
router.register('usuarios', UsuariosCustomizadosViewSet, basename='Usuarios')
router.register('tecnologias', TecnologiasViewSet, basename='Tecnologias')
router.register('projetos', ProjetosViewSet, basename='Projetos')
router.register('login', LoginViewSet, basename='Login')

urlpatterns = [
    path('', include(router.urls)),
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
