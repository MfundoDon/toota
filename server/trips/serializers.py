from rest_framework import serializers
from .models import Trip
from authentication.serializers import UserSerializer, DriverSerializer


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'
        read_only_fields = ('id', 'created', 'updated')









    



        
        



        

                