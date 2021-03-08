from django.core.paginator import Paginator
from rest_framework.views import APIView
from rest_framework import permissions, status
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sadmin.models import Country, Division, District, SubDistrict, AssignDataCollector, CollectData, ServiceCategory, \
    Package, Surveyor, STATUS_CHOICES
from sadminapi.serializers import CountrySerializer, DivisionSerializer, DistrictSerializer, SubDistrictSerializer, \
    AssignmentSerializer, DataCollectFormSerializer, DataListSerializer, DataDetailsSerializer, ServiceListSerializer, \
    PackageListSerializer, UserDetailsSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime


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
        surveyor = Surveyor.objects.get(user_id=self.request.user.id)
        assignments = AssignDataCollector.objects.filter(data_collector=surveyor)[::-1]
        serializer = AssignmentSerializer(assignments, many=True)

        data_list = list()
        for data in assignments:
            data_dict = dict({'company_name': data.company_name,
                              'service_category_id': data.service_category.id,
                              'service_category': data.service_category.name,
                              'assign_by': data.assign_by,
                              'created_at': data.created_at,
                              'area': data.area
                              })
            data_list.append(data_dict)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': data_list,
                'user_id': self.request.user.id,
                'surveyor_id': surveyor.id
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': 'Empty List',
                'data': [],
                'user_id': self.request.user.id,
                'surveyor_id': surveyor.id
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)


class DataCollectForm(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        # serializer = DataCollectFormSerializer(data=request.data)

        try:
            visited_company_name = request.data.get("visited_company_name")
            contact_person_name = request.data.get("contact_person_name")
            designation_of_contact_person = request.data.get("designation_of_contact_person")
            service_category = request.data.get("service_category")
            service_category_obj = ServiceCategory.objects.get(id=service_category)
            package_name = request.data.get("package_name")
            package_name_obj = Package.objects.get(id=package_name)
            contact_no = request.data.get("contact_no")
            email = request.data.get("email")
            address = request.data.get("address")
            picture_visited_person = request.FILES.get("picture_visited_person")
            picture_of_visiting_card = request.FILES.get("picture_of_visiting_card")
            description = request.data.get("description")
            company_review = request.data.get('company_review')
            collector_obj = CollectData(data_collector=request.user, visited_company_name=visited_company_name,
                                        contact_person_name=contact_person_name,
                                        designation_of_contact_person=designation_of_contact_person,
                                        service_category_id=service_category, package_name_id=package_name,
                                        contact_no=contact_no, email=email, address=address,
                                        picture_visited_person=picture_visited_person,
                                        picture_of_visiting_card=picture_of_visiting_card, description=description,
                                        company_review=company_review)

            collector_obj.save()

            response = {
                'status_code': status.HTTP_201_CREATED,
                'message': 'Successfully created',
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_201_CREATED)
        except Exception as e:
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': str(e),
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


class UserDetails(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        surveyor_details = Surveyor.objects.get(user_id=self.request.user.id)

        data_dict = {
            "username": surveyor_details.user.username,
            "firstname": surveyor_details.user.first_name,
            "lastname": surveyor_details.user.last_name,
            "email": surveyor_details.email,
            "designation": surveyor_details.designation,
            "area": surveyor_details.area,
            "address": surveyor_details.address,
            "profile_picture": surveyor_details.profile_picture.url,
            "phone": surveyor_details.phone,
            "total_submitted_form": CollectData.objects.filter(data_collector_id=self.request.user.id).count()
        }

        serializer = UserDetailsSerializer(surveyor_details)

        if serializer.data:
            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': data_dict,
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


class AllSummary(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data_dict = {
                'total_registered_agent': Surveyor.objects.count(),
                'total_active_agent': Surveyor.objects.filter(status=STATUS_CHOICES[0].index('Active')).count(),
                'total_collected_data': CollectData.objects.count()
            }

            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': data_dict,
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': str(e),
                'data': [],
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_404_NOT_FOUND)


class CollectionDataByDate(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, date):
        try:
            filter_date = datetime.strptime(date, '%Y-%m-%d')
            data_list_date = CollectData.objects.filter(created_at__day=filter_date.day,
                                                        created_at__month=filter_date.month,
                                                        created_at__year=filter_date.year)

            data_list = list()
            for data in data_list_date:
                data_dict = {
                    'data_collector_username': data.data_collector.username,
                    'data_collector_name': data.data_collector.first_name + ' ' + data.data_collector.last_name,
                    'company_name': data.visited_company_name,
                    'address': data.address,
                    'created_at': data.created_at,
                    'company_review': data.company_review
                }

                data_list.append(data_dict)

            response = {
                'status_code': status.HTTP_200_OK,
                'message': 'Success',
                'data': data_list,
                'user_id': self.request.user.id
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'status_code': status.HTTP_404_NOT_FOUND,
                'message': str(e),
                'data': [],
                'user_id': self.request.user.id
            }

            return Response(response, status=status.HTTP_404_NOT_FOUND)



