from socket import fromshare
from django import forms
from .models import Sender
from .models import Packet
from .models import Receiver

class SenderForm(forms.ModelForm):
    class Meta:
        model=Sender
        fields="__all__"

class PacketForm(forms.ModelForm):
    class Meta:
        model=Packet
        fields="__all__"

class ReceiverForm(forms.ModelForm):
    class Meta:
        model=Receiver
        fields="__all__"