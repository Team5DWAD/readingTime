# Generated by Django 2.2.17 on 2021-04-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingTime', '0006_auto_20210404_1409'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='UploadImage',
            field=models.FileField(upload_to='ContactImg'),
        ),
    ]
