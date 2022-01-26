from rest_framework import serializers
from .models import Job, Application

class ApplicationSerializer(serializers.ModelSerializer):
  ''' Serializer for outgoing job response '''

  class Meta:
        model = Application
        fields = '__all__'
        


class JobSerializer(serializers.ModelSerializer):
    ''' Serializer for outgoing job response '''
    applications = ApplicationSerializer(many=True, read_only=True)

    class Meta:
        model = Job
        fields = '__all__'
        