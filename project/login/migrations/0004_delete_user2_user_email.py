# Generated by Django 5.0.1 on 2024-02-07 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_user2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User2',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
