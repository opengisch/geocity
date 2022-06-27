# Generated by Django 3.2.13 on 2022-06-27 07:15

import ckeditor.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import permits.fields


class Migration(migrations.Migration):

    dependencies = [
        ("reports", "0002_create_default_reports"),
    ]

    operations = [
        migrations.CreateModel(
            name="SectionAmendProperty",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Commentaire·s des services",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionContact",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Contact·s",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionDetail",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Détail·s",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionHorizontalRule",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Ligne horizontale",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionPlanning",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Planning",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionStatus",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Statut",
            },
            bases=("reports.section",),
        ),
        migrations.CreateModel(
            name="SectionValidation",
            fields=[
                (
                    "section_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="reports.section",
                    ),
                ),
            ],
            options={
                "verbose_name": "Commentaire·s du secrétariat",
            },
            bases=("reports.section",),
        ),
        migrations.AlterModelOptions(
            name="sectionauthor",
            options={"verbose_name": "Auteur"},
        ),
        migrations.AlterModelOptions(
            name="sectionmap",
            options={"verbose_name": "Carte"},
        ),
        migrations.AlterModelOptions(
            name="sectionparagraph",
            options={"verbose_name": "Paragraphe libre"},
        ),
        migrations.AlterField(
            model_name="sectionmap",
            name="qgis_print_template_name",
            field=models.CharField(blank=True, default="a4", max_length=30),
        ),
        migrations.AlterField(
            model_name="sectionmap",
            name="qgis_project_file",
            field=permits.fields.AdministrativeEntityFileField(
                blank=True,
                storage=permits.fields.PrivateFileSystemStorage(),
                upload_to="qgis_templates",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["qgs"]
                    )
                ],
                verbose_name="Projet QGIS '*.qgs'",
            ),
        ),
        migrations.AlterField(
            model_name="sectionparagraph",
            name="content",
            field=ckeditor.fields.RichTextField(
                help_text='Il est possible d\'inclure des variables et de la logique avec la <a href="https://jinja.palletsprojects.com/en/3.1.x/templates/">syntaxe Jinja</a>. Les variables de la demande sont accessible dans `{{request_data}}` et clles du work object type dans `{{wot_data}}`.'
            ),
        ),
    ]
