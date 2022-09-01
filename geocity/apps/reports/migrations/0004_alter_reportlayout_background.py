# Generated by Django 3.2.13 on 2022-06-28 06:50

import django.core.validators
from django.db import migrations

from geocity.apps import permits


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0003_use_privatestorage_for_report_background_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="reportlayout",
            name="background",
            field=permits.fields.AdministrativeEntityFileField(
                blank=True,
                null=True,
                storage=permits.fields.PrivateFileSystemStorage(),
                upload_to="report_layout_backgrounds",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["png", "jpg"]
                    )
                ],
                verbose_name='Image d\'arrière plan ("papier à en-tête")',
            ),
        ),
    ]
