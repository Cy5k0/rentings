# Generated by Django 5.1.3 on 2024-11-21 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0006_alter_tipousuario_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tipousuario',
            name='tipo',
            field=models.CharField(choices=[('1', 'Arrendador'), ('2', 'Arrendatario')], default='Nulo', max_length=20),
        ),
    ]
