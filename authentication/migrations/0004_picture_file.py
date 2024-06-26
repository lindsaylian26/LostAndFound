# Generated by Django 5.0.3 on 2024-03-17 19:18

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='file',
            field=models.FileField(default=None, storage=storages.backends.s3.S3Storage(), upload_to='uploads/'),
        ),
    ]
