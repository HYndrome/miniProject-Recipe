# Generated by Django 3.2.18 on 2023-05-05 12:58

from django.db import migrations, models
import reviews.models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewphoto',
            name='image_review',
            field=models.ImageField(upload_to=reviews.models.ReviewPhoto.image_path),
        ),
    ]