from sadmin.models import Country, Division, District, SubDistrict, AssignDataCollector, CollectData, ServiceCategory, \
    Package, Surveyor
from rest_framework import serializers


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = ['division_name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['district_name']


class SubDistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDistrict
        fields = ['sub_district_name']


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignDataCollector
        fields = ['company_name', 'service_category', 'assign_by', 'created_at', 'area']


class DataCollectFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectData
        fields = ['data_collector', 'visited_company_name', 'contact_person_name', 'designation_of_contact_person',
                  'service_category', 'contact_no', 'email', 'address', 'picture_visited_person', 'package_name',
                  'description', 'created_at', 'company_review']


class DataListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectData
        fields = ['data_collector', 'visited_company_name', 'contact_person_name', 'designation_of_contact_person',
                  'service_category', 'contact_no', 'email', 'address', 'picture_visited_person',
                  'picture_of_visiting_card', 'package_name', 'description', 'created_at', 'company_review']


class DataDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CollectData
        fields = ['data_collector', 'visited_company_name', 'contact_person_name', 'designation_of_contact_person',
                  'service_category', 'contact_no', 'email', 'address', 'picture_visited_person', 'package_name',
                  'description', 'created_at', 'company_review']


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = ['name', 'id']


class PackageListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Package
        fields = ['name', 'id', 'service_category_id']


class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Surveyor
        fields = ['address', 'profile_picture', 'country', 'division', 'district', 'sub_district', 'email',
                  'graduation_subject', 'university', 'skills', 'area', 'phone', 'description', 'designation',
                  'experience', 'role', 'created_at', 'status']

