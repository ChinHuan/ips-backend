# Generated by Django 3.1 on 2020-10-11 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_auto_20201010_1443'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tagID', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
