from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import viewsets
from email.policy import HTTP
#from itertools import product
from pdb import post_mortem
from webbrowser import get

#from app.serializers import SenderSerializer
from .models import Receiver, Sender
from .models import Packet
from .forms import SenderForm
from .forms import PacketForm
from .forms import ReceiverForm
from .serializers import SenderSerializer
from .serializers import ReceiverSerializer
from .serializers import PacketSerializer

def index(request):
	return HttpResponse("Hola Mundo")

def contacto(request,name):
	return HttpResponse(f"Bienvenido {name} a la clase de Django")

#def sender(request):
#	sender=Sender.objects.all()
#	return render(request,"senders.html",{
#		"senders":sender
#	})

def sender(request):
	#post_ciNIt=request.POST.get('ciNit')
	#if post_ciNIt:
	#	q=Sender(ciNit=post_ciNIt)
	#	q.save()
	filtro_ciNit=request.GET.get("ciNit")
	if filtro_ciNit:
		sender=Sender.objects.filter(ciNit__contains=filtro_ciNit)
	else:
		sender=Sender.objects.all()
		
	print(sender.query)
	return render(request,"senders.html",{
		"senders":sender
	})

def senderFormView(request):
	form=SenderForm()
	sender=None

	id_sender=request.GET.get('id')
	if id_sender:
		#sender=Sender.objects.filter(id=id_sender)
		sender=get_object_or_404(Sender,id=id_sender)
		form = SenderForm(instance=sender)

	if request.method == 'POST':
		if sender:
			form=SenderForm(request.POST,instance=sender)
		else:
			form= SenderForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request,"form_senders.html",{
		"form":form
	})


def packetFormView(request):
	form=PacketForm()
	packet=None

	id_packet=request.GET.get('id')
	if id_packet:
		packet=get_object_or_404(Packet,id=id_packet)
		form = PacketForm(instance=packet)

	if request.method == 'POST':
		if packet:
			form=PacketForm(request.POST,instance=packet)
		else:
			form= PacketForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request,"form_packets.html",{
		"form":form
	})

def receiverFormView(request):
	form=ReceiverForm()
	receiver=None

	id_receiver=request.GET.get('id')
	if id_receiver:
		receiver=get_object_or_404(Receiver,id=id_receiver)
		form = ReceiverForm(instance=receiver)

	if request.method == 'POST':
		if receiver:
			form=ReceiverForm(request.POST,instance=receiver)
		else:
			form= ReceiverForm(request.POST)
	if form.is_valid():
		form.save()
	return render(request,"form_receiver.html",{
		"form":form
	})


class SenderViewSet(viewsets.ModelViewSet):
	queryset=Sender.objects.all()
	serializer_class=SenderSerializer

class ReceiverViewSet(viewsets.ModelViewSet):
	queryset=Receiver.objects.all()
	serializer_class=ReceiverSerializer

class PacketViewSet(viewsets.ModelViewSet):
	queryset=Packet.objects.all()
	serializer_class=PacketSerializer