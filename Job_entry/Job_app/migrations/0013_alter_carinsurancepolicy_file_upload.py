# Generated by Django 4.2.3 on 2023-10-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0012_alter_carinsurancepolicy_file_upload'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carinsurancepolicy',
            name='file_upload',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
