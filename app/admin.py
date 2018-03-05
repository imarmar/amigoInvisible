from .models import Participant
from django.contrib import admin

class ParticipantAdmin(admin.options.ModelAdmin):
    list_display = [
                    'name',
                    'email',
                    'partner',
                    'user'
                    ]
    search_fields = ['name']
 
admin.site.register(Participant, ParticipantAdmin)
