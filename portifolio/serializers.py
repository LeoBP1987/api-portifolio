from rest_framework import serializers
from portifolio.models import UsuariosCustomizados, Tecnologias, Projetos
import json

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

    def get_descricoes_conteudo(self, obj):
        
        if obj.descricoes and obj.descricoes.path:
            try:
                with open(obj.descricoes.path, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except Exception as e:
                print(f"Erro ao ler o arquivo descricoes: {e}")
                return None
        return None