# Generated by Django 2.1.3 on 2018-11-16 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0007_auto_20181114_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='max_players',
            field=models.IntegerField(),
        ),
    ]
