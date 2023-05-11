from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.permissions import AllowAny
from accounts.serializers import UserRegisterSerializer 
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from accounts.utils.token import create_tokens
from rest_framework import status
from rest_framework.exceptions import ValidationError
# Create your views here.


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')
    if not email or not password:
        raise ValidationError(
            detail='email and password if required', code=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(email__exact=email)
        if not user.check_password(raw_password=password):
            raise ValidationError(detail='User credentials are not valid',
                                  code=status.HTTP_400_BAD_REQUEST)
        access_token, refresh_token = create_tokens(user=user)
        data = {
            'access_token': access_token,
            'refresh_token': refresh_token,
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    except User.DoesNotExist:
        raise ValidationError(detail='User credentials are not valid',
                              code=status.HTTP_404_NOT_FOUND)
    

class UserRegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        request.data['is_active'] = True
        request.data['password'] = make_password(request.data['password'])
        return super(UserRegisterView, self).create(request, *args, **kwargs)


   