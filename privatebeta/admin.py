from django.contrib import admin
from privatebeta.models import InviteRequest

class InviteRequestAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('email', 'created', 'invited',)
    list_filter = ('created', 'invited',)

admin.site.register(InviteRequest, InviteRequestAdmin)
