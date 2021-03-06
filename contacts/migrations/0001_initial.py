# Generated by Django 3.0.1 on 2019-12-20 09:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listing', models.CharField(max_length=255)),
                ('listing_id', models.IntegerField()),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('contact_date', models.DateTimeField(default=datetime.datetime.now)),
                ('contact_id', models.IntegerField(blank=True)),
            ],
        ),
    ]
