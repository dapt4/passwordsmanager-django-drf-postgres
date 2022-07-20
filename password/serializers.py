from rest_framework import serializers
from .models import Password

class PasswordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Password
        fields = ['id','host', 'username', 'email', 'passwrd']

