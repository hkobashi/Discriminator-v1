# Generated by Django 3.2.9 on 2022-03-21 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_review_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='image',
        ),
        migrations.AddField(
            model_name='review',
            name='appendedPicture',
            field=models.ImageField(null=True, upload_to='reviewPicture'),
        ),
    ]
