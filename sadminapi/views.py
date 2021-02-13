from rest_framework.views import APIView
from rest_framework import permissions
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from sadmin.models import Country
from sadminapi.serializers import CountrySerializer


class CountryList(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)
