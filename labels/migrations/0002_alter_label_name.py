# Generated by Django 5.2.3 on 2025-06-25 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='label',
            name='name',
            field=models.CharField(max_length=255, unique=True, verbose_name='Имя'),
        ),
    ]
