# Generated by Django 5.1.6 on 2025-05-22 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0004_login"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Login",
            new_name="LoginData",
        ),
    ]
