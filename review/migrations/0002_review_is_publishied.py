# Generated by Django 3.2.9 on 2022-02-03 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='is_publishied',
            field=models.BooleanField(default=False),
        ),
    ]