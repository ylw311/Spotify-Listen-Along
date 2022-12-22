from rest_framework import serializers
from .models import Room

# serialize as a response we can return
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')

# serialize a request, return in python format
# make sure data sent in POST request is valid and fits the field we need  to create a new room
class CreateRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('guest_can_pause', 'votes_to_skip')


# Note:
# when handling requests: good idea to use serializer to handle request (incoming) or handle response (outgoing)