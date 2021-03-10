# Generated by Django 3.1.4 on 2021-01-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0011_works_object_properties_date_input"),
    ]

    operations = [
        migrations.AddField(
            model_name="permitactortype",
            name="is_mandatory",
            field=models.BooleanField(default=True, verbose_name="obligatoire"),
        ),
        migrations.AlterField(
            model_name="historicalpermitactor",
            name="company_name",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Entreprise"
            ),
        ),
        migrations.AlterField(
            model_name="permitactor",
            name="company_name",
            field=models.CharField(
                blank=True, max_length=100, verbose_name="Entreprise"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="permitactortype", unique_together={("type", "works_type")},
        ),
    ]