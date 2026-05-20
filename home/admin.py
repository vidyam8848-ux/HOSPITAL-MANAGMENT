from django.contrib import admin

# Register your models here.
from . models import dept,Doctors,booking

admin.site.register(dept)
admin.site.register(Doctors)
admin.site.register(booking)


