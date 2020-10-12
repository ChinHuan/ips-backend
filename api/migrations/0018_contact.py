# Generated by Django 3.1 on 2020-10-12 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_coordinate_inclosecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('contactID', models.AutoField(primary_key=True, serialize=False)),
                ('datetime', models.DateTimeField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.place')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tag')),
            ],
        ),
    ]
