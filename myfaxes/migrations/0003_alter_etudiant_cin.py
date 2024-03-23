# Generated by Django 5.0.3 on 2024-03-23 05:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myfaxes', '0002_filiere_alter_cours_code_alter_sujet_type_sujet_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etudiant',
            name='cin',
            field=models.CharField(max_length=8, validators=[django.core.validators.RegexValidator('^\\d{8}$', 'Entrez un numéro CIN valide.')]),
        ),
    ]