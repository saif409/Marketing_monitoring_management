from sadmin.models import Country, Division, District, SubDistrict, AssignDataCollector
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
        fields = ['company_name', 'purpose_of_visit', 'assign_by', 'created_at']




