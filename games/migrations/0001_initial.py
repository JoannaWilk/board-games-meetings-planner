# Generated by Django 2.1.3 on 2018-11-19 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('mod_date', models.DateTimeField(auto_now=True)),
                ('min_players', models.IntegerField()),
                ('max_players', models.IntegerField()),
                ('game_type', models.CharField(choices=[('SG', 'Strategy'), ('DB', 'Deck Building'), ('AG', 'Adventures')], max_length=1)),
                ('description', models.TextField(null=True)),
            ],
        ),
    ]
