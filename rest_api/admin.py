from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from rest_framework.authtoken.models import Token

from rest_api.models.adoption import AdoptionRequest
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.models.colaboration import Colaboration
from rest_api.models.complaint import Complaint
from rest_api.models.profile import Profile
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter

from rest_api.models.refugio_event import RefugioEvent
from rest_api.models.timeline import Timeline
from rest_api.services.refugio_event import RefugioEventService


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'
    max_num = 1
    verbose_name = 'Perfil'

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            fieldsets = super(CustomUserAdmin, self).get_fieldsets(request, obj)
        else:
            fieldsets = (
                (None, {
                    'fields': ('username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser',)
                }),)
        return fieldsets

    def has_delete_permission(self, request, obj=None):
        if obj is not None and obj.is_superuser:
            return request.user.is_superuser
        if obj is not None and obj.is_staff:
            return request.user.is_superuser
        return True

    def has_change_permission(self, request, obj=None):
        if obj is not None and obj.is_superuser:
            return request.user.is_superuser
        if obj is not None and obj.is_staff:
            return request.user.is_superuser
        return True

    def get_readonly_fields(self, request, obj=None):
        print(obj.__dict__)
        if request.user.is_superuser:
            return super(CustomUserAdmin, self).get_readonly_fields(request, obj)
        else:
            if obj is not None and obj.is_superuser:
                return 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_superuser'
            return 'username', 'email', 'is_staff', 'is_superuser'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None, renderer=None):
        output = []

        if value and getattr(value, "url", None):
            image_url = value.url
            file_name = str(value)

            output.append(
                f' <a href="{image_url}" target="_blank">'
                f'  <img src="{image_url}" alt="{file_name}" width="150" height="150" '
                f'style="object-fit: cover;"/> </a>')

        output.append(super(AdminFileWidget, self).render(name, value, attrs, renderer))
        return mark_safe(u''.join(output))


class InlineImage(admin.TabularInline):
    model = ImageAnimal
    formfield_overrides = {
        models.ImageField: {'widget': AdminImageWidget}
    }
    extra = 0


class AnimalAdmin(admin.ModelAdmin):
    inlines = [InlineImage]
    list_display = ('name', 'species', 'race',)
    list_filter = (
        ('name', DropdownFilter),
        ('species', DropdownFilter),
        ('race', DropdownFilter),
    )


class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'animal_solicitado', 'potencial_adoptante')
    # list_select_related = ('animal','potencial_adopter')
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('potencial_adopter__user__email', DropdownFilter),
        ('animal__species', DropdownFilter), # adopter_requests
        ('animal__name', DropdownFilter),
        ('animal__race', DropdownFilter),
    )

    def get_queryset(self, request):
        return super(AdoptionRequestAdmin, self).get_queryset(request).prefetch_related('animal', 'potencial_adopter')

    def save_model(self, request, obj, form, change):
        super(AdoptionRequestAdmin, self).save_model(request, obj, form, change)
        RefugioEventService.modify_adoption_request_event(adoption_request=obj, requester_email=request.user.email)


class RefugioEventAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'cambio_realizado_por')

    list_filter = (
        ('reported_by__user__email', DropdownFilter),
    )

    def lookup_allowed(self, lookup, value):
        return True

    def get_queryset(self, request):
        return super(RefugioEventAdmin, self).get_queryset(request).prefetch_related('reported_by')


class InlineRefugioEvent(admin.TabularInline):
    model = RefugioEvent
    extra = 0


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'animal_asociado')
    inlines = (InlineRefugioEvent,)
    list_filter = (
        ('animal__name', DropdownFilter),
    )

    def lookup_allowed(self, lookup, value):
        return True

    def get_queryset(self, request):
        return super(TimelineAdmin, self).get_queryset(request).prefetch_related('animal')


class ColaborationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    filter_horizontal = ('colaborators',)


admin.site.site_header = "Refugio App Backoffice"
admin.site.site_title = "Backoffice Portal"
admin.site.index_title = "Bienvenidos a Refugio App"

admin.site.unregister(Token)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
admin.site.register(Complaint)
admin.site.register(RefugioEvent, RefugioEventAdmin)
admin.site.register(Colaboration, ColaborationAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AdoptionRequest, AdoptionRequestAdmin)