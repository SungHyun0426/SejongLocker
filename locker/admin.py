from django.contrib import admin
from .models import Locker

# Register your models here.
class ViewLocker(admin.ModelAdmin):
    list_display = ('user', 'lockerId', 'availability')

admin.site.register(Locker, ViewLocker)
