# Generated by Django 3.0.5 on 2020-04-23 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discussion',
            old_name='data_creation',
            new_name='creation_date',
        ),
    ]
