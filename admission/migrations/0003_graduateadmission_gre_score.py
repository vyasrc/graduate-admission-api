# Generated by Django 2.2.4 on 2019-12-24 00:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admission', '0002_remove_graduateadmission_gre_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='graduateadmission',
            name='gre_score',
            field=models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)]),
            preserve_default=False,
        ),
    ]