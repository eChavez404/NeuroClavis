import uuid
from django.db import models
from datetime import date

import uuid
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser, BaseUserManager # <-- Novos imports

class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(unique=True) 

    USERNAME_FIELD = 'email' # Avisa o Django que o Email é o login!
    REQUIRED_FIELDS = [] # O email já é obrigatório por padrão

    objects = UsuarioManager()

    def __str__(self):
        return self.email

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Diagnostico(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.nome

class Paciente(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    diagnostico_principal = models.ForeignKey(Diagnostico, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def idade_atual(self):
        hoje = date.today()
        return hoje.year - self.data_nascimento.year - ((hoje.month, hoje.day) < (self.data_nascimento.month, self.data_nascimento.day))

    def __str__(self):
        return f"{self.nome} - Code: {str(self.id)[:6]}"

class SessaoJogo(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='sessoes')

    tempo_primeira_acao = models.FloatField()
    tempo_total = models.FloatField()
    cliques_falsos = models.IntegerField()
    solturas_erradas = models.IntegerField()
    qtd_quedas = models.IntegerField()
    tempo_segurando_peca = models.FloatField()
    cliques_frustracao = models.IntegerField()
    tempo_congelado_pos_erro = models.FloatField()

    laudo_ia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Sessão de {self.paciente.nome} em {self.created_at.strftime('%d/%m/%Y')}"

class NivelLog(models.TextChoices):
    INFO = 'INFO', 'Informação'
    WARNING = 'WARNING', 'Aviso'
    ERROR = 'ERROR', 'Erro Crítico'

class RegistroLog(TimeStampedModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nivel = models.CharField(max_length=10, choices=NivelLog.choices, default=NivelLog.INFO)
    acao = models.CharField(max_length=255)
    detalhes = models.TextField(blank=True, null=True)
    ip_origem = models.GenericIPAddressField(blank=True, null=True)

    class Meta:
        verbose_name = 'Registro de Log'
        verbose_name_plural = 'Painel de Logs'
        ordering = ['-created_at']

    def __str__(self):
        return f"[{self.nivel}] {self.acao} - {self.created_at.strftime('%d/%m/%Y')}"