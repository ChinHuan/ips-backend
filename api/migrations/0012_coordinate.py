# Generated by Django 3.1 on 2020-10-08 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_place_placephotourl'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('coordinateID', models.AutoField(primary_key=True, serialize=False)),
                ('tagID', models.CharField(max_length=10)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
            ],
        ),
    ]
