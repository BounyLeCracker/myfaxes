# Generated by Django 5.0.3 on 2024-03-23 07:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfaxes', '0004_alter_sujet_type_sujet'),
    ]

    operations = [
        migrations.AddField(
            model_name='cours',
            name='niveau',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myfaxes.niveau'),
        ),
    ]
