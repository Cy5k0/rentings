# Generated by Django 5.1.3 on 2024-11-19 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestion_inmuebles', '0007_remove_tipousuario_nombre_tipousuario_tipo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='estado',
            field=models.BooleanField(default=True),
        ),
    ]