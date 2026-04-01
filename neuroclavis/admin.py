from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Diagnostico, Paciente, SessaoJogo, RegistroLog, Usuario

# 1. INLINES (Sessões dentro do Paciente)
class SessaoJogoInline(admin.StackedInline):
    model = SessaoJogo
    extra = 0
    readonly_fields = ('laudo_ia',)

# 2. REGISTRO DAS TABELAS PRINCIPAIS
@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'created_at')

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'data_nascimento', 'diagnostico_principal', 'created_at')
    search_fields = ('nome',)
    inlines = [SessaoJogoInline]

@admin.register(SessaoJogo)
class SessaoJogoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'created_at', 'tempo_total', 'qtd_quedas')
    list_filter = ('paciente', 'created_at')
    readonly_fields = ('laudo_ia',)

@admin.register(RegistroLog)
class RegistroLogAdmin(admin.ModelAdmin):
    list_display = ('nivel', 'acao', 'created_at', 'ip_origem')
    list_filter = ('nivel', 'created_at')
    search_fields = ('acao', 'detalhes')
    
    def has_add_permission(self, request): return False
    def has_change_permission(self, request, obj=None): return False
    def has_delete_permission(self, request, obj=None): return False

# 3. FORMULÁRIO DE CRIAÇÃO SEGURA DE USUÁRIO (Níveis e Senhas)
class UsuarioCreationForm(forms.ModelForm):
    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirme a senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('email', 'is_staff', 'is_superuser', 'groups')

    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não conferem.")
        return senha2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha1"])
        if commit:
            user.save()
            self.save_m2m() # Salva a relação de Grupos
        return user

# 4. REGISTRO DO USUÁRIO NO PAINEL
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    add_form = UsuarioCreationForm 
    model = Usuario
    
    ordering = ['email']
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'senha1', 'senha2', 'is_staff', 'is_superuser', 'groups')}
        ),
    )