from django.db import models
from uuid import uuid4

class Cliente(models.Model):
    id_cliente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, null=False, blank=True)
    sobrenome = models.CharField(max_length=255, null=False, blank=True)
    cpf = models.CharField(max_length=14, null=False, blank=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    celular = models.CharField(max_length=255, null=False, blank=True)
    rua = models.CharField(max_length=255, null=False, blank=True)
    numero = models.IntegerField(null=False, blank=True)
    bairro = models.CharField(max_length=255, null=False, blank=True)
    cidade = models.CharField(max_length=255, null=False, blank=True)
    cadastro = models.DateField(auto_now_add=True)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.nome


    '''
    slug = models.SlugField(max_length=255)
    SlugField é o texto da url ex. www.meusite.com.br/texto-do-slug
    '''
