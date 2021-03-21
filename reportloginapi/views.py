from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework import permissions
from reportloginapi.serializers import UserSerializer, GroupSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)

            response = {
                'status_code': status.HTTP_200_OK,
                'token': token.key,
                'user_id': user.id
            }
            return Response(response, status=status.HTTP_200_OK)

        except Exception as e:
            response = {
                'status_code': status.HTTP_400_BAD_REQUEST,
                'message': 'Username and password doesn\'t match'
            }
            return Response(response, status=status.HTTP_400_BAD_REQUEST)


custom_auth_token = CustomAuthToken.as_view()


class Logout(APIView):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)