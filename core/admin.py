from django.contrib import admin

# Register your models here.
from .models import Position, Services, Member


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'active', 'modify')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_title', 'icon', 'active', 'modify')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'active', 'modify')
