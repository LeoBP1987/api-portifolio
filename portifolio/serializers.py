from rest_framework import serializers
from portifolio.models import UsuariosCustomizados, Tecnologias, Projetos

class UsuariosCustomizadosSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuariosCustomizados
        fields = ('nome_completo', 'username', 'email', 'descricao', 'sobreMim', 'foto_perfil')

class TecnologiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologias
        fields = '__all__'

class ProjetosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = '__all__'