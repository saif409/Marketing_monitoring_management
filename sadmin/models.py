from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver


# Create your models here.
ROLE_CHOICES = (
    (1, 'Admin'),
    (2, 'Supervisor'),
    (3, 'User'),
)

REVIEW_CHOICES = (
    (1, 'OneStar'),
    (2, 'TwoStar'),
    (3, 'ThreeStar'),
    (4, 'FourStar'),
    (5, 'FiveStar'),
)

STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'InActive'),
    (3, 'Rejected'),
)


class Surveyor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='user_info')
    address = models.CharField(max_length=200)
    profile_picture = models.ImageField()
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
    sub_district_name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.sub_district_name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Package(models.Model):
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, name='service_category')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class CollectData(models.Model):
    data_collector = models.ForeignKey(User, on_delete=models.CASCADE)
    visited_company_name = models.CharField(max_length=200)
    contact_person_name = models.CharField(max_length=200)
    designation_of_contact_person = models.CharField(max_length=200)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.DO_NOTHING)
    package = models.ForeignKey(Package, on_delete=models.DO_NOTHING)
    contact_no = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    picture_visited_person = models.ImageField(null=True)
    picture_of_visiting_card = models.ImageField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    company_review = models.IntegerField(choices=REVIEW_CHOICES)
    longitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.visited_company_name


class AssignDataCollector(models.Model):
    company_name = models.CharField(max_length=200)
    service_category = models.ForeignKey(ServiceCategory, on_delete=models.DO_NOTHING)
    data_collector = models.ForeignKey(Surveyor, on_delete=models.DO_NOTHING)
    assign_by = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    division = models.ForeignKey(Division, on_delete=models.DO_NOTHING)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    sub_district = models.ForeignKey(SubDistrict, on_delete=models.DO_NOTHING)
    area = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.company_name


class NoticeBoard(models.Model):
    title = models.CharField(max_length=200)
    notice_desc = models.CharField(max_length=1000)
    notice_image = models.ImageField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, auto_now=False)


class AuthLogs(models.Model):
    action = models.CharField(max_length=64)
    ip = models.GenericIPAddressField(null=True)
    app_username = models.CharField(max_length=256, null=True, blank=True)
    user_fullname = models.CharField(max_length=256, null=True, blank=True)
    device_username = models.CharField(max_length=256, null=True, blank=True)
    device_name = models.CharField(max_length=256, null=True, blank=True)
    operating_system = models.CharField(max_length=256, null=True, blank=True)
    request_sender_app = models.CharField(max_length=256, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)

    def __unicode__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.action, self.username, self.ip)


@receiver(user_logged_in)
def user_logged_in_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    user_fullname = user.first_name + " " + user.first_name
    device_name = request.META.get('COMPUTERNAME')
    device_username = request.META.get('USERNAME')
    operating_system = request.META.get('OS')
    request_sender_app = request.META.get('HTTP_USER_AGENT')

    AuthLogs.objects.create(action='user_logged_in', ip=ip, user_fullname=user_fullname, app_username=user.username, device_name=device_name,
                            device_username=device_username, operating_system=operating_system,
                            request_sender_app=request_sender_app)


@receiver(user_logged_out)
def user_logged_out_callback(sender, request, user, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    user_fullname = user.first_name + " " + user.last_name
    device_name = request.META.get('COMPUTERNAME')
    device_username = request.META.get('USERNAME')
    operating_system = request.META.get('OS')
    request_sender_app = request.META.get('HTTP_USER_AGENT')

    AuthLogs.objects.create(action='user_logged_out', ip=ip, user_fullname=user_fullname, app_username=user.username, device_name=device_name,
                            device_username=device_username, operating_system=operating_system,
                            request_sender_app=request_sender_app)


@receiver(user_login_failed)
def user_login_failed_callback(sender, request, credentials, **kwargs):
    ip = request.META.get('REMOTE_ADDR')
    device_name = request.META.get('COMPUTERNAME')
    device_username = request.META.get('USERNAME')
    operating_system = request.META.get('OS')
    request_sender_app = request.META.get('HTTP_USER_AGENT')

    AuthLogs.objects.create(action='user_login_failed', ip=ip, app_username=credentials.get('username', None),
                            device_name=device_name, device_username=device_username,
                            operating_system=operating_system, request_sender_app=request_sender_app)