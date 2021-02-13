from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# Create your models here.
ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Supervisor'),
    (3, 'User'),
)

REVIEW_CHOICES = (
    (1, 'Onestar'),
    (2, 'Twostar'),
    (3, 'Threestar'),
    (4, 'fourstar'),
    (5, 'fivestar'),
)

STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'InActive'),
    (3, 'Rejected'),
)


class Surveyor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='user_info')
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField(null=True,blank=True)
    country = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    sub_district = models.CharField(max_length=100)
    email = models.CharField(max_length=100,null=True, blank=True)
    graduation_subject = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    skills = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = models.TextField()
    designation = models.CharField(max_length=100)
    experience = models.CharField(max_length=200)
    role = models.IntegerField(choices=ROLE_CHOICES, null=True, default=3)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=True, default=2)

    def __str__(self):
        return str(self.user)


class Country(models.Model):
    country_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.country_name


class Division(models.Model):
    division_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.division_name


class District(models.Model):
    district_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.district_name


class SubDistrict(models.Model):
    subdistrct_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.subdistrct_name


class CollectData(models.Model):
    data_collector = models.ForeignKey(User,null = True, on_delete=models.CASCADE)
    visited_company_name = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    designation_of_contact_person = models.CharField(max_length=200)
    purpose_of_visit = models.CharField(max_length=200)
    contact_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    picture_visited_person = models.FileField()
    picture_of_visiting_card = models.FileField(null=True)
    package_name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    company_review = models.IntegerField(choices=REVIEW_CHOICES)

    def __str__(self):
        return self.visited_company_name


class AssignDataCollector(models.Model):
    company_name = models.CharField(max_length=200)
    purpose_of_visit = models.CharField(max_length=200)
    assign_data_collector = models.ForeignKey(User, on_delete=models.CASCADE)
    assign_by = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    sub_district = models.ForeignKey(SubDistrict, on_delete=models.CASCADE)
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)


    def __str__(self):
        return self.company_name