# Generated by Django 4.1 on 2022-10-05 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicio',
            old_name='image',
            new_name='imagen',
        ),
    ]