# Generated by Django 5.0.1 on 2024-02-07 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_signin'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Signin',
            new_name='Signup',
        ),
    ]
