# Generated by Django 2.2.6 on 2019-11-02 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoproject', '0002_post_institute'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='instructor_image',
            field=models.ImageField(default='default.jpg', upload_to='instructor_images'),
        ),
    ]
