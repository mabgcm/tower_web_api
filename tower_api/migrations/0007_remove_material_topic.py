# Generated by Django 4.1.1 on 2022-09-24 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tower_api', '0006_rename_title_material_topic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='material',
            name='topic',
        ),
    ]
