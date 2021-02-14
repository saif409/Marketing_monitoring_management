from rest_framework.views import APIView
from rest_framework import permissions
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sadmin.models import Country, Division, District, SubDistrict
from sadminapi.serializers import CountrySerializer, DivisionSerializer, DistrictSerializer, SubDistrictSerializer


class CountryList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class DivisionList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        divisions = Division.objects.all()
        serializer = DivisionSerializer(divisions, many=True)
        return Response(serializer.data)


class DistrictList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)
        return Response(serializer.data)


class SubDistrictList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sub_districts = SubDistrict.objects.all()
        serializer = SubDistrictSerializer(sub_districts, many=True)
        return Response(serializer.data)



