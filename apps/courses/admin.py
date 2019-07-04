from django.contrib import admin

from apps.courses.models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ['email', 'invoice', 'created', 'updated']


admin.site.register(Order, OrderAdmin)
