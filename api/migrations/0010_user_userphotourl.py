# Generated by Django 3.1 on 2020-08-22 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_auto_20200812_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='userPhotoUrl',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
