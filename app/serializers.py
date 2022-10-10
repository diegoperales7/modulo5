from dataclasses import field
from rest_framework import serializers 
from .models import Sender
from .models import Receiver
from .models import Packet


class SenderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sender
        fields="__all__"

class ReceiverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Receiver
        fields="__all__"

class PacketSerializer(serializers.ModelSerializer):
    class Meta:
        model=Packet
        fields="__all__"