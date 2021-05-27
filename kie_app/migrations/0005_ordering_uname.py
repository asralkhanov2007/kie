# Generated by Django 3.2.3 on 2021-05-27 11:40

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('kie_app', '0004_remove_ordering_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordering',
            name='uname',
            field=models.CharField(default=datetime.datetime(2021, 5, 27, 11, 40, 59, 653269, tzinfo=utc), max_length=150, verbose_name='Name of user'),
            preserve_default=False,
        ),
    ]