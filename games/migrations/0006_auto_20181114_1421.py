# Generated by Django 2.1.3 on 2018-11-14 13:21

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_auto_20181114_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='added_by',
            field=models.ForeignKey(default=1, on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
    ]
