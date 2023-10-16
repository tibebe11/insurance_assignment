# Generated by Django 4.2.3 on 2023-10-06 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0010_carinsurancepolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='carinsurancepolicy',
            name='email',
            field=models.EmailField(default='tibebetilahun11@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='carinsurancepolicy',
            name='file_upload',
            field=models.FileField(default=None, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='carinsurancepolicy',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
