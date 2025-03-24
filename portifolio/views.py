from rest_framework import viewsets, filters
from portifolio.models import UsuariosCustomizados, Tecnologias, Projetos
from portifolio.serializers import UsuariosCustomizadosSerializer, TecnologiasSerializer, ProjetosSerializer
from django_filters.rest_framework import DjangoFilterBackend

class UsuariosCustomizadosViewSet(viewsets.ModelViewSet):
    queryset = UsuariosCustomizados.objects.all().order_by('username')
    serializer_class = UsuariosCustomizadosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]

class TecnologiasViewSet(viewsets.ModelViewSet):
    queryset = Tecnologias.objects.all().order_by('nome')
    serializer_class = TecnologiasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome', ]

class ProjetosViewSet(viewsets.ModelViewSet):
    queryset = Projetos.objects.all().order_by('nome')
    serializer_class = ProjetosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['id' ,'nome', ]
