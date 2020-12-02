# Generated by Django 3.1.3 on 2020-12-02 08:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_project_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='contentscore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='creativityscore',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='project',
            name='rating',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='project',
            name='userabilityscore',
            field=models.IntegerField(default=0),
        ),
    ]
