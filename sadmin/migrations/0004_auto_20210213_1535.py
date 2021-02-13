# Generated by Django 3.1.6 on 2021-02-13 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sadmin', '0003_delete_area'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectdata',
            old_name='picture',
            new_name='picture_visited_person',
        ),
        migrations.AddField(
            model_name='collectdata',
            name='company_review',
            field=models.IntegerField(choices=[(1, 'Onestar'), (2, 'Twostar'), (3, 'Threestar'), (4, 'fourstar'), (5, 'fivestar')], default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='collectdata',
            name='picture_of_visiting_card',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
