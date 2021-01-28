# Generated by Django 3.1.4 on 2021-01-28 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0014_needs_date_and_geometry_checks"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="worksobjectproperty",
            options={
                "ordering": ["order"],
                "verbose_name": "1.5 Configuration du champ",
                "verbose_name_plural": "1.5 Configuration des champs",
            },
        ),
        migrations.AddField(
            model_name="worksobjectproperty",
            name="order",
            field=models.PositiveIntegerField(default=0, verbose_name="ordre"),
        ),
    ]
