# Generated by Django 4.1.7 on 2023-03-22 15:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0003_fotografia_publicado'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='criado_em',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 22, 12, 54, 40, 747841)),
        ),
    ]
