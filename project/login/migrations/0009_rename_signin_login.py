# Generated by Django 5.0.1 on 2024-02-07 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0008_remove_signin_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signin',
            new_name='Login',
        ),
    ]