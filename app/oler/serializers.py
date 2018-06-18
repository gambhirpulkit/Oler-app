from .models import User, RideHistory, RideTrack
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'first_name', 'last_name', 'is_driver', 'is_rider')


class RideHistorySerializer(serializers.ModelSerializer):
    driver_name = serializers.CharField(source="driver.username", required=False)

    class Meta:
        model = RideHistory
        fields = ('ride_type', 'active', 'driver_name')


class RideRequestSerializer(serializers.ModelSerializer):
    d_id = serializers.IntegerField(source="driver_id", read_only=False, required=False)
    driver_name = serializers.CharField(source="driver.first_name", read_only=False, required=False)

    class Meta:
        model = RideHistory
        fields = ('id', 'ride_type', 'active', 'd_id', 'driver_name')


class RideTrackSerializer(serializers.ModelSerializer):
    h_id = serializers.IntegerField(source="history_id", read_only=False, required=False)
    r_id = serializers.IntegerField(source="rider_id", read_only=False, required=False)
    rider_name = serializers.CharField(source="rider.first_name", read_only=False, required=False)
    driver_name = serializers.CharField(source="history.driver.first_name", read_only=False, required=False)

    class Meta:
        model = RideTrack
        fields = ('id', 'ride_state', 'h_id', 'r_id', 'rider_name', 'seats', 'driver_name')