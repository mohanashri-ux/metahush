# Generated by Django 5.1.6 on 2025-06-26 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0017_remove_petsittingservice_cost'),
    ]

    operations = [
        migrations.RenameField(
            model_name='petsittingservice',
            old_name='SITTING_TYPE_CHOICES',
            new_name='sitting_type',
        ),
    ]
