# Generated by Django 4.1.6 on 2023-02-18 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incluir', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrada',
            options={'ordering': ['data']},
        ),
    ]
