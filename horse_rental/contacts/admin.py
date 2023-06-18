from django.contrib import admin
from contacts.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'text')
    search_fields = ('user', )
    list_filter = ('date', )
    readonly_fields = ('date', )
    list_editable = ('text', )
    fields = ('user', 'date', 'text')

