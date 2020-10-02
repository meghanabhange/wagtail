# Generated by Django 3.1.1 on 2020-10-02 17:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0056_streampage_nested_streamblock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdocument',
            name='file',
            field=models.FileField(upload_to='documents', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=None)], verbose_name='file'),
        ),
    ]