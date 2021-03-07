# Generated by Django 3.1.6 on 2021-02-17 06:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('district_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SubDistrict',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_district_name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Surveyor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('country', models.CharField(max_length=100)),
                ('division', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('sub_district', models.CharField(max_length=100)),
                ('email', models.CharField(blank=True, max_length=100, null=True)),
                ('graduation_subject', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('skills', models.CharField(max_length=200)),
                ('area', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('designation', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=200)),
                ('role', models.IntegerField(choices=[(1, 'Admin'), (2, 'Supervisor'), (3, 'User')], default=3, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(1, 'Active'), (2, 'InActive'), (3, 'Rejected')], default=2, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('service_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.servicecategory')),
            ],
        ),
        migrations.CreateModel(
            name='CollectData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_company_name', models.CharField(max_length=200)),
                ('contact_person_name', models.CharField(max_length=200)),
                ('designation_of_contact_person', models.CharField(max_length=200)),
                ('service_category', models.CharField(max_length=200)),
                ('contact_no', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('picture_visited_person', models.FileField(upload_to='')),
                ('picture_of_visiting_card', models.FileField(null=True, upload_to='')),
                ('package_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_review', models.IntegerField(choices=[(1, 'Onestar'), (2, 'Twostar'), (3, 'Threestar'), (4, 'fourstar'), (5, 'fivestar')], null=True)),
                ('data_collector', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AssignDataCollector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=200)),
                ('service_category', models.CharField(max_length=200)),
                ('assign_by', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data_collector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.country')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.district')),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.division')),
                ('sub_district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sadmin.subdistrict')),
            ],
        ),
    ]
