from django.contrib import admin

from horse_reg.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_create', 'date_update')
    search_fields = ('user', )
    list_filter = ('date_create', 'date_update')
    readonly_fields = ('date_create', 'date_update', 'user')
    fields = ('user', 'img', 'phone', 'body', 'date_create', 'date_update')
