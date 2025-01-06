from django.contrib import admin
from .models import Contact, Image
from  django.contrib.auth.models  import  Group  

admin.site.register((Contact,Image))
admin.site.unregister(Group) 