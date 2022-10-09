from email.policy import HTTP
from django.shortcuts import render
from django.http import HttpResponse
from .models import Sender

def index(request):
	return HttpResponse("Hola Mundo")

def contacto(request,name):
	return HttpResponse(f"Bienvenido {name} a la clase de Django")

def sender(request):
	sender=Sender.objects.all()
	return render(request,"senders.html",{
		"senders":sender
	})