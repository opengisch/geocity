# Generated by Django 2.2.6 on 2020-05-20 09:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permits', '0015_permit_request_status_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='permitrequest',
            name='printed_at',
            field=models.DateTimeField(null=True, verbose_name="date d'impression"),
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='printed_by',
            field=models.CharField(blank=True, max_length=255, verbose_name='imprimé par'),
        ),
        migrations.AddField(
            model_name='permitrequest',
            name='printed_file',
            field=models.FileField(blank=True, upload_to='printed_permits/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='permis imprimé'),
        ),
    ]