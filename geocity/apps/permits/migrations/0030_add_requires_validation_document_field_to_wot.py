# Generated by Django 3.2.4 on 2021-07-07 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("permits", "0029_visibility_of_secreatariat_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="worksobjecttype",
            name="requires_validation_document",
            field=models.BooleanField(
                default=True, verbose_name="Document de validation obligatoire"
            ),
        ),
    ]