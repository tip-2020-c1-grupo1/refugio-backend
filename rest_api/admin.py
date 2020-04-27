from django.contrib import admin
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.models.profile import Profile


class InlineImage(admin.TabularInline):
    model = ImageAnimal


class AnimalAdmin(admin.ModelAdmin):
    inlines = [InlineImage]


class ProfileAdmin(admin.ModelAdmin):
    model = Profile


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Animal, AnimalAdmin)