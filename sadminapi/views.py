from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import permissions, status
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sadmin.models import Country, Division, District, SubDistrict, AssignDataCollector, CollectData, ServiceCategory, Package
from sadminapi.serializers import CountrySerializer, DivisionSerializer, DistrictSerializer, SubDistrictSerializer, \
    AssignmentSerializer, DataCollectFormSerializer, DataListSerializer, DataDetailsSerializer, ServiceListSerializer, \
    PackageListSerializer
from django.shortcuts import get_object_or_404


class CountryList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class DivisionList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        divisions = Division.objects.all()
        serializer = DivisionSerializer(divisions, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class DistrictList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        districts = District.objects.all()
        serializer = DistrictSerializer(districts, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

class SubDistrictList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        sub_districts = SubDistrict.objects.all()
        serializer = SubDistrictSerializer(sub_districts, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class AssignmentList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        assignments = AssignDataCollector.objects.filter(assign_data_collector=self.request.user)[::-1]
        serializer = AssignmentSerializer(assignments, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class DataCollectForm(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = DataCollectFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': 'Successfully created',
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_201_CREATED)

        response = {
            'status_code': status.HTTP_400_BAD_REQUEST,
            'message': serializer.errors,
            'user_id': self.request.user.id
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)


class DataList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        data_list = CollectData.objects.filter(data_collector=self.request.user)
        serializer = DataListSerializer(data_list, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class DataDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        data_details = CollectData.objects.filter(id=id)
        serializer = DataDetailsSerializer(data_details, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class ServiceList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        service_list = ServiceCategory.objects.all()[::-1]
        serializer = ServiceListSerializer(service_list, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class PackageList(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, id):
        package_list = Package.objects.filter(service_category_id=id)
        serializer = PackageListSerializer(package_list, many=True)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': serializer.data,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)