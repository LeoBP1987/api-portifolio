from rest_framework import viewsets, filters, status
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.response import Response
from rest_framework.decorators import action, api_view
from portifolio.models import UsuariosCustomizados, Tecnologias, Projetos
from portifolio.serializers import UsuariosCustomizadosSerializer, TecnologiasSerializer, ProjetosSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
import os
import requests

class UsuariosCustomizadosViewSet(viewsets.ModelViewSet):
    queryset = UsuariosCustomizados.objects.all().order_by('username')
    serializer_class = UsuariosCustomizadosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    permission_classes = [IsAuthenticatedOrReadOnly]

class TecnologiasViewSet(viewsets.ModelViewSet):
    queryset = Tecnologias.objects.all().order_by('nome')
    serializer_class = TecnologiasSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['nome', ]
    search_fields = ['nome', ]
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjetosViewSet(viewsets.ModelViewSet):
    queryset = Projetos.objects.all().order_by('ordem')
    serializer_class = ProjetosSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['ordem', ]
    search_fields = ['id' ,'nome', ]
    permission_classes = [IsAuthenticatedOrReadOnly]

class LoginViewSet(viewsets.ViewSet):
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'], url_path='get-login')
    def oauth_login(self, request):
        data = request.data

        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            return Response({"error": "Username e password são obrigatórios"}, status=status.HTTP_400_BAD_REQUEST)

        payload = {
            'client_id': str(os.getenv('ClientId')),
            'client_secret': str(os.getenv('ClientSecret')),
            'grant_type': 'password',
            'username': username,
            'password': password
        }

        try:
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}
            response = requests.post('https://api-portifolio-f4f0784e5e08.herokuapp.com/oauth2/token/', data=payload, headers=headers)
            response.raise_for_status() 
            token_data = response.json()

            try:
                usuario_id = UsuariosCustomizados.objects.get(username=username).id
            except ObjectDoesNotExist:
                return Response({"error": "Usuário não encontrado"}, status=status.HTTP_404_NOT_FOUND)

            return Response({
                'access_token': token_data['access_token'],
                'refresh_token': token_data.get('refresh_token', ''),
                'user_id': usuario_id
            }, status=status.HTTP_200_OK)

        except requests.exceptions.RequestException as e:
            return Response({"error": f"Falha ao obter token de acesso: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST'])
def enviar_contato(request):
    try:
        data = request.data
        
        if not all([data.get('nome'), data.get('email'), data.get('mensagem')]):
            return Response({'erro': 'Todos os campos são obrigatórios'}, status=status.HTTP_400_BAD_REQUEST)
        
        assunto = f"Mensagem de contato de {data['nome']}"
        mensagem = f"""
        Nome: {data['nome']}
        Email: {data['email']}
        Mensagem:
        {data['mensagem']}
        """
        remetente = data['email']
        destinatario = [settings.EMAIL_HOST_USER]
        
        send_mail(
            assunto,
            mensagem,
            remetente,
            destinatario,
            fail_silently=False,
        )
        
        return Response({'sucesso': 'Mensagem enviada com sucesso'}, status=status.HTTP_200_OK)
    
    except Exception as e:
        return Response({'erro': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
