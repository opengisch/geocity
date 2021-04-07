# Generated by Django 3.1.4 on 2021-03-31 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0017_permit_request_amend_custom_fields'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='permitadministrativeentity',
            options={'permissions': [('see_private_requests', 'Voir les demandes restreintes')], 'verbose_name': "1.1 Configuration de l'entité administrative (commune, organisation)", 'verbose_name_plural': "1.1 Configuration de l'entité administrative (commune, organisation)"},
        ),
        migrations.AddField(
            model_name='worksobjecttype',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Public'),
        ),
    ]
