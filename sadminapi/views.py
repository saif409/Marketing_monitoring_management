from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import permissions, status
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sadmin.models import Country, Division, District, SubDistrict, AssignDataCollector, CollectData, ServiceCategory
from sadminapi.serializers import CountrySerializer, DivisionSerializer, DistrictSerializer, SubDistrictSerializer, \
    AssignmentSerializer, DataCollectFormSerializer, DataListSerializer, DataDetailsSerializer, ServiceListSerializer


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


class AssignmentList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        assignments = AssignDataCollector.objects.filter(assign_data_collector=self.request.user)[::-1]
        serializer = AssignmentSerializer(assignments, many=True)
        return Response(serializer.data)


class DataCollectForm(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        serializer = DataCollectFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DataList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data_list = CollectData.objects.filter(data_collector=self.request.user)
        serializer = DataListSerializer(data_list, many=True)
        return Response(serializer.data)


class DataDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        data_details = CollectData.objects.filter(id=id)
        serializer = DataDetailsSerializer(data_details, many=True)
        return Response(serializer.data)


class ServiceList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        service_list = ServiceCategory.objects.all()[::-1]
        serializer = ServiceListSerializer(service_list, many=True)
        return Response(serializer.data)




