# Generated by Django 3.2.9 on 2022-03-20 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0006_auto_20220314_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
