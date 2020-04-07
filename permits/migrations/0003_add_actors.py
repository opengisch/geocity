# Generated by Django 2.2.6 on 2020-01-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpf', '0029_auto_20191115_0801'),
        ('permits', '0002_add_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='permitrequest',
            name='actors',
            field=models.ManyToManyField(related_name='_permitrequest_actors_+', to='gpf.Actor'),
        ),
    ]
