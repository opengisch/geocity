# Generated by Django 3.2.12 on 2022-04-05 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0061_anonymous_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='worksobjecttype',
            name='is_anonymous_available',
            field=models.BooleanField(default=False, verbose_name='Supporte les demandes anonymes'),
        ),
    ]
