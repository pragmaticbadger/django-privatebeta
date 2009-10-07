from django.contrib import admin
from privatebeta.models import InviteRequest

class InviteRequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('email', 'created')
    list_filter = ('created',)

admin.site.register(InviteRequest, InviteRequestAdmin)
