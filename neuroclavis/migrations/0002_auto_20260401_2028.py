from django.db import migrations
from django.contrib.auth.hashers import make_password

def gerar_seed_admin(apps, schema_editor):
    # Pega exatamente a sua tabela customizada 'Usuario' do app 'neuroclavis'
    Usuario = apps.get_model('neuroclavis', 'Usuario')
    
    email = 'admin@gmail.com'
    
    # Verifica se já existe para não quebrar caso rode o migrate duas vezes
    if not Usuario.objects.filter(email=email).exists():
        Usuario.objects.create(
            email=email,
            # make_password criptografa a senha forçadamente, ignorando a regra de 8 caracteres
            password=make_password('Clavis'),
            is_staff=True,
            is_superuser=True,
            is_active=True
        )

def reverter_seed(apps, schema_editor):
    Usuario = apps.get_model('neuroclavis', 'Usuario')
    Usuario.objects.filter(email='admin@gmail.com').delete()

class Migration(migrations.Migration):

    dependencies = [
        # MUITO IMPORTANTE: Garanta que isso aponta para a sua migration inicial
        ('neuroclavis', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(gerar_seed_admin, reverter_seed),
    ]