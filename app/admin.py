from django.contrib import admin
from .models import Sender
from .models import Receiver
from .models import Address
from .models import Packet
from .models import Status
from .models import Service

# Register your models here.

admin.site.register(Sender)
admin.site.register(Receiver)
admin.site.register(Address)
admin.site.register(Packet)
admin.site.register(Status)
admin.site.register(Service)


