# Generated by Django 3.1.6 on 2021-03-06 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0005_auto_20210306_1312'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assigndatacollector',
            old_name='assign_data_collector',
            new_name='data_collector',
        ),
    ]
