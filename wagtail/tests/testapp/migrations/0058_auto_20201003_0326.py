# Generated by Django 3.1.1 on 2020-10-02 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0057_auto_20201003_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customdocument',
            name='file',
            field=models.FileField(upload_to='documents', verbose_name='file'),
        ),
    ]
