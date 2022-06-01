from django.contrib import admin
from .models import Team


# Register your models here.

class AdminTeam(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Team, AdminTeam)
