# Generated by Django 3.1.3 on 2021-01-06 13:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20210105_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 8, 13, 22, 50, 292854, tzinfo=utc)),
        ),
    ]
