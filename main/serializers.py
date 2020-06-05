from rest_framework import serializers

from main import models
#from models import Activity_peroid

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = '__all__'

class Activity_peroidSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Activity_peroid
        fields = '__all__'


