# Generated by Django 2.1.3 on 2018-11-14 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('games', '0003_auto_20181114_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='added_by',
            field=models.ForeignKey(null=True, on_delete=models.SET('deleted'), to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='owners',
            field=models.ManyToManyField(related_name='owned_games', to=settings.AUTH_USER_MODEL),
        ),
    ]
