from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username',
                  'email','password', 'is_active')
        extra_kwargs = {
            'password': {'write_only': True}
        }

        