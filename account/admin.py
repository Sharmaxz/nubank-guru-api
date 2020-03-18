from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import User


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'date', 'message')


class MyUserAdmin(UserAdmin):
    search_fields = ('email',)
    list_display = ('email', 'first_name', 'is_staff')
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ("Personal information", {'fields': ('first_name', 'last_name',)}),
        ("Permissions", {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        ("Activity", {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, MyUserAdmin)