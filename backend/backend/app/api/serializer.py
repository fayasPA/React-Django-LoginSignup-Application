from rest_framework import serializers
from ..models import *


class MyUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'last_name', 'username', 'phone_number', 'email', 'password', 'image']

