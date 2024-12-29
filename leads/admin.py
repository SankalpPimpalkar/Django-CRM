from django.contrib import admin
from .models import CustomUser, Lead, Agent

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Lead)
admin.site.register(Agent)