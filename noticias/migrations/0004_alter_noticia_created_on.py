# Generated by Django 3.2.9 on 2021-12-02 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_alter_noticia_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
