# Generated by Django 5.0.3 on 2024-06-01 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DRP', '0002_remove_entrepot_central_responsable_entrepot_central_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='depot',
            name='telephone_depot',
        ),
        migrations.RemoveField(
            model_name='entrepot_central',
            name='email_entrepot_central',
        ),
        migrations.RemoveField(
            model_name='entrepot_central',
            name='telephone_entrepot_central',
        ),
    ]
