# Generated by Django 5.0.1 on 2024-02-10 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_rename_email_signup_signup_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kandidat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto1', models.ImageField(blank=True, null=True, upload_to='kandidat/')),
                ('nama_kandidat1', models.CharField(max_length=100)),
                ('foto2', models.ImageField(blank=True, null=True, upload_to='kandidat/')),
                ('nama_kandidat2', models.CharField(max_length=100)),
            ],
        ),
    ]
