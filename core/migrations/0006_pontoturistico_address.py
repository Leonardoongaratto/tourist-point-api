# Generated by Django 4.0.5 on 2022-06-08 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
        ('core', '0005_pontoturistico_assesment'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='address',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='address.endereco'),
            preserve_default=False,
        ),
    ]