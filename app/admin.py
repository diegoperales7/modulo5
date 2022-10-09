from django.contrib import admin
from .models import Sender
from .models import Receiver
from .models import Address
from .models import Packet
from .models import Status
from .models import Service

# Register your models here.

class SenderAdmin(admin.ModelAdmin):
    list_display= ("fullName","ciNit","phoneNumber","email")

class ReceiverAdmin(admin.ModelAdmin):
    list_display= ("fullName","ciNit","phoneNumber","email")

class AddressAdmin(admin.ModelAdmin):
    list_display= ("address","city","latitude","longitude")

class PacketAdmin(admin.ModelAdmin):
    list_display= ("type","description","price","address","sender","receiver")

class StatusAdmin(admin.ModelAdmin):
    list_display= ("type","packet","created","updated")

#class ServiceAdmin(admin.ModelAdmin):
 #   list_display= ("type")

admin.site.register(Sender,SenderAdmin)
admin.site.register(Receiver,ReceiverAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Packet,PacketAdmin)
admin.site.register(Status,StatusAdmin)
admin.site.register(Service)


