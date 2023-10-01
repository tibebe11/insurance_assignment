# Generated by Django 4.2.4 on 2023-08-11 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Job_app', '0007_job_jobapplication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='testimonial_images')),
                ('client_name', models.CharField(max_length=255)),
                ('profession', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='abouttext',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='abouttext',
            name='image_3',
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]