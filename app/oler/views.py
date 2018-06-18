from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, RideHistory, RideTrack
from .serializers import UserSerializer, RideHistorySerializer, RideRequestSerializer, RideTrackSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# Get details of all rides by a user/driver
class RideHistoryView(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            if user.is_rider:
                history_ids = RideTrack.objects.filter(rider=user).values_list('history_id', flat=True)
                history = RideHistory.objects.filter(id__in=history_ids)
            else:
                history = RideHistory.objects.filter(driver=user)
            return history
        except User.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        history = self.get_object(pk)
        serializer = RideHistorySerializer(history, many=True)
        return Response(serializer.data)


# Book a new ride
class RideRequestView(APIView):
    def post(self, request):

        # Later called from request.user when session is maintained
        rider_id = request.data['rider_id']
        driver_id = request.data['driver_id']
        ride_type = int(request.data['ride_type'])
        seats = int(request.data['seats'])

        driver = User.objects.get(pk=driver_id)

        ride_history = RideHistory.objects.filter(driver=driver, active=True).order_by('-created_at')
        if ride_history.exists():
            ride_history = ride_history.first()
            ride_track = RideTrack.objects.filter(history_id=ride_history.id)
            if ride_history.ride_type == RideHistory.MINI_GO:
                return Response({"Driver not available"}, status=status.HTTP_303_SEE_OTHER)
            elif ride_history.ride_type == RideHistory.SHARE and ride_history.seats + seats > 4:
                return Response({"Driver not available"}, status=status.HTTP_303_SEE_OTHER)
            else:
                updated_seats = ride_history.seats + seats
                serializer = RideRequestSerializer(ride_history, data={"seats": updated_seats})
                if serializer.is_valid():
                    serializer.save()
                    # Todo track serializer
                return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            serializer = RideRequestSerializer(
                data={"d_id": driver_id, "ride_type": ride_type, "seats": seats, "active": True}
            )

            if serializer.is_valid():
                serializer.save()
                track_serializer = RideTrackSerializer(
                    data={"h_id": serializer.data['id'], "ride_state": RideTrack.REQUESTED, "r_id": rider_id})
                if track_serializer.is_valid():
                    track_serializer.save()

                    data_dict = serializer.data
                    data_dict.update(track_serializer.data)
                    return Response(data_dict, status=status.HTTP_201_CREATED)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


# Update status of existing ride using ride history id
class RideTrackView(APIView):
    def post(self, request):

        rider_id = request.data['rider_id']
        history_id = int(request.data['history_id'])
        ride_state = int(request.data['ride_state'])

        ride_track = RideTrack.objects.filter(history=history_id, ride_state=ride_state).order_by('-created_at')

        if ride_track.exists():
            return Response({"Status already updated."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            track_serializer = RideTrackSerializer(
                data={"h_id": history_id, "ride_state": ride_state, "r_id": rider_id}
            )
            if track_serializer.is_valid():
                track_serializer.save()
                if ride_state == RideTrack.COMPLETED or ride_state == RideTrack.REJECTED:
                    history = RideHistory.objects.get(pk=history_id)
                    data = {"active": False}
                    history_serializer = RideHistorySerializer(history, data)
                    if history_serializer.is_valid():
                        history_serializer.save()
                return Response(track_serializer.data, status=status.HTTP_201_CREATED)

# # Update profile of driver using his id
# class DriverProfileUpdateView(APIView):
#     def get_object(self, pk):
#         try:
#             return Dr.objects.get(pk=pk)
#         except RideHistory.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk):
#         history = self.get_object(pk)
#         serializer = RideRequestSerializer(history)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         history = self.get_object(pk)
#         serializer = RideRequestSerializer(history, request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
