from django.urls import path
from . import views

urlpatterns=[

	path('contacto/<str:name>',views.contacto, name='contacto'),
	path('',views.index, name='index'),
	path('senders/',views.sender, name='sender'),
]