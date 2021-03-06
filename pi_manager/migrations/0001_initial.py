# Generated by Django 2.0.3 on 2018-04-03 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100)),
                ('drive_id', models.CharField(max_length=64, unique=True)),
                ('certificate', models.CharField(max_length=10)),
                ('status', models.IntegerField(choices=[(0, 'normal'), (1, 'off line'), (2, 'lost'), (3, 'unknown error')])),
            ],
        ),
    ]
