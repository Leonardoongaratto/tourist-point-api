# Generated by Django 4.0.5 on 2022-06-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attractions', '0001_initial'),
        ('core', '0002_alter_pontoturistico_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='attraction',
            field=models.ManyToManyField(to='attractions.atracao'),
        ),
    ]
