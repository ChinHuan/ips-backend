# Generated by Django 3.0.8 on 2020-07-10 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200710_1839'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=20)),
                ('role', models.IntegerField(choices=[(1, 'User'), (2, 'Admin')])),
            ],
        ),
    ]
