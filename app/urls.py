from decimal import DefaultContext
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
router.register(r"senders",views.SenderViewSet)
router.register(r"receivers",views.ReceiverViewSet)
router.register(r"packets",views.PacketViewSet)

urlpatterns=[

	#path('contacto/<str:name>',views.contacto, name='contacto'),
	#path('',views.index, name='index'),
	#path('senders/',views.sender, name="senders"),
	#path('senders/',views.senderFormView, name="senders"),
	#path('packets/',views.packetFormView, name="packets"),
	#path('receivers/',views.receiverFormView, name="receivers"),

	#path('senders/fullName?<str:fullName>',views.sender, name='sender'),

	path('',include(router.urls))
]