from django.db import migrations

def set_site_domain(apps, schema_editor):
    Site = apps.get_model('sites', 'Site')
    Site.objects.update_or_create(
        id=1,
        defaults={
            'domain': 'webapp-produtos-2026-accnc8czdwhydxbt.brazilsouth-01.azurewebsites.net',
            'name': 'Cadastro de Produtos'
        }
    )

class Migration(migrations.Migration):
    dependencies = [
        ('produtos', '0001_initial'),
        ('sites', '0002_alter_domain_unique'),
    ]
    operations = [
        migrations.RunPython(set_site_domain),
    ]