from django.contrib import admin
from .models import *

class SubscriberAdmin (admin.ModelAdmin):
    list_display = ["email", "name", "id"]
    list_filter = ["name", ]
    search_fields = ["email", "name", "id"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)