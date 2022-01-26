from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Job, Application

User = get_user_model()

class NestedUserSerializer(serializers.ModelSerializer):

  class Meta:
    model = User
    fields = ('id', 'username')

class ApplicationSerializer(serializers.ModelSerializer):
  ''' Serializer for Applications '''

  class Meta:
        model = Application
        fields = '__all__'

class NestedApplicationSerializer(serializers.ModelSerializer):
  ''' Serializer for Applications Nested '''
  owner = NestedUserSerializer()

  class Meta:
        model = Application
        fields = '__all__'        


class JobSerializer(serializers.ModelSerializer):
    ''' Serializer for outgoing job response '''
    applications = NestedApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        