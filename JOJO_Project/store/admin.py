from pyexpat import model
from django.contrib import admin


from . import models

# Register your models here.
from .models import Booking, Contact, Gateau, Album
admin.site.register(Booking)
admin.site.register(Contact)

admin.site.register(Album)


@admin.register(models.Gateau)
class GateauAdmin(admin.ModelAdmin):
    filter_horizontal = ('albums',)