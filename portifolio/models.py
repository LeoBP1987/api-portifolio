from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField

class UsuariosCustomizados(AbstractUser):
    nome_completo=models.CharField(max_length=150, null=False, blank=False)
    username=models.CharField(max_length=150, null=False, blank=False, unique=True)
    email=models.EmailField(max_length=150, null=False, blank=False, unique=True)
    password=models.CharField(max_length=150, null=False, blank=False)
    descricao=models.TextField(max_length=600, null=False, blank=False)
    sobreMim = ArrayField(
        models.TextField(blank=True, null=True),
        blank=True,
        null=True,
        default=list
    )
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

class Tecnologias(models.Model):
    nome=models.CharField(max_length=150, null=False, blank=False)
    tipo=ArrayField(
        models.CharField(max_length=150, null=False, blank=False),
        blank=False,
        null=False,
        default=list
    )
    iconeOriginal=models.FileField(upload_to='iconesTech/Originais/', null=False, blank=False)
    iconeEstilizado=models.FileField(upload_to='iconesTech/Estilizados/', null=False, blank=False)

class Projetos(models.Model):
    nome=models.CharField(max_length=150, null=False, blank=False)
    imagem_capa=models.ImageField(upload_to='imagens_capa/', null=False, blank=False)
    descricaoCurta=models.TextField(max_length=300, null=False, blank=False)
    descricaoLonga=models.TextField()
    linkVideoDemonstracao=models.URLField(max_length=300)
    imagemDemonstracao=models.ImageField(upload_to='imagens_demonstracao/', null=False, blank=False)
    descricaoBackEnd=models.TextField()
    descricaoFrontEnd=models.TextField()
    stacks=ArrayField(
        models.CharField(blank=True, null=True),
        blank=True,
        null=True,
        default=list
    )
    linkDeploy=models.URLField(max_length=300)
    linkCodigoFonte=models.URLField(max_length=300)