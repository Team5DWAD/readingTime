# Generated by Django 2.2.17 on 2021-04-04 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('readingTime', '0004_auto_20210404_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='UploadImage',
            field=models.ImageField(upload_to='UploadImage'),
        ),
    ]
