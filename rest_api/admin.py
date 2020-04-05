from django.contrib import admin
from .models import Animal, ImageAnimal

#from rest_framework.authtoken.admin import TokenAdmin

#TokenAdmin.raw_id_fields = ('user',)

# Register your models here.

class InlineImage(admin.TabularInline):
    model = ImageAnimal


class AnimalAdmin(admin.ModelAdmin):
    inlines = [InlineImage]

admin.site.register(Animal, AnimalAdmin)