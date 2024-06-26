# Generated by Django 5.0.3 on 2024-03-17 22:25

import storages.backends.s3
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_picture_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='file',
            field=models.FileField(default=None, storage=storages.backends.s3.S3Storage(), upload_to='imageUpload/'),
        ),
    ]
