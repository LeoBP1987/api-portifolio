from django.utils.safestring import mark_safe
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
    descricaoLonga = serializers.SerializerMethodField()
    descricaoBackEnd = serializers.SerializerMethodField()
    descricaoFrontEnd = serializers.SerializerMethodField()

    def get_descricaoLonga(self, obj):
        return mark_safe(obj.descricaoLonga) if obj.descricaoLonga else None
    
    def get_descricaoBackEnd(self, obj):
        return mark_safe(obj.descricaoBackEnd) if obj.descricaoBackEnd else None
    
    def get_descricaoFrontEnd(self, obj):
        return mark_safe(obj.descricaoFrontEnd) if obj.descricaoFrontEnd else None

    class Meta:
        model = Projetos
        fields = '__all__'