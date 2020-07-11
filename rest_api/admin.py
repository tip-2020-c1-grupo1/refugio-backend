import csv

from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib import admin
from django.db import models
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from rest_framework.authtoken.models import Token

from rest_api.models.adoption import AdoptionRequest
from rest_api.models.animals import Animal, ImageAnimal, AnimalSpecie
from rest_api.models.colaboration import Colaboration, ColaborationColaborators
from rest_api.models.complaint import Complaint
from rest_api.models.profile import Profile
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter, ChoiceDropdownFilter

from rest_api.models.refugio_event import RefugioEvent
from rest_api.models.timeline import Timeline
from rest_api.services.colaboration import ColaborationRequestService
from rest_api.services.refugio_event import RefugioEventService


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fk_name = 'user'
    max_num = 1
    verbose_name = 'Perfil'

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser


class CustomUserAdmin(UserAdmin, ExportCsvMixin):
    inlines = (ProfileInline,)
    actions = ["export_as_csv"]

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


class AnimalAdminForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class AnimalAdmin(admin.ModelAdmin, ExportCsvMixin):
    inlines = [InlineImage]
    list_display = ('name', 'race', 'especie_animal')
    form = AnimalAdminForm
    list_filter = (
        ('name', DropdownFilter),
        ('species__name', DropdownFilter),
        ('race', DropdownFilter),
    )
    readonly_fields = ['status_request', ]
    actions = ["export_as_csv"]


class AdoptionRequestAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'animal_solicitado', 'potencial_adoptante')
    # list_select_related = ('animal','potencial_adopter')
    list_filter = (
        ('status', ChoiceDropdownFilter),
        ('potencial_adopter__user__email', DropdownFilter),
        ('animal__species__name', DropdownFilter),  # adopter_requests
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
    readonly_fields = ['title', 'timeline']

    def lookup_allowed(self, lookup, value):
        return True

    def get_queryset(self, request):
        return super(RefugioEventAdmin, self).get_queryset(request).prefetch_related('reported_by')


class InlineRefugioEvent(admin.TabularInline):
    model = RefugioEvent
    extra = 0
    readonly_fields = (
        'title',
        'description',
        'timeline',
        'reported_by',
        'metadata',
        'date_created',
        'date_modified'
    )


class TimelineAdmin(admin.ModelAdmin):
    list_display = ('pk', 'description', 'animal_asociado')
    inlines = (InlineRefugioEvent,)
    list_filter = (
        ('animal__name', DropdownFilter),
    )
    readonly_fields = ('animal',)

    def lookup_allowed(self, lookup, value):
        return True

    def get_queryset(self, request):
        return super(TimelineAdmin, self).get_queryset(request).prefetch_related('animal')


class InlineColaborationColaborators(admin.TabularInline):
    model = ColaborationColaborators
    extra = 0


class ColaborationColaboratorsAdmin(admin.ModelAdmin):
    readonly_fields = ['colaborator', 'colaboration']


class ColaborationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    # filter_horizontal = ('colaborators',)
    inlines = (InlineColaborationColaborators,)
    readonly_fields = ['satisfied',  'status_request']

    def save_formset(self, request, form, formset, change):
        formset.save()
        for f in formset.forms:
            obj = f.instance
            colaboration = Colaboration.objects.get(pk=obj.colaboration_id)
            ColaborationRequestService.change_status_colaboration(colaboration)


class ComplaintAdmin(admin.ModelAdmin):
    model = Profile


admin.site.site_header = "Refugio App Backoffice"
admin.site.site_title = "Backoffice Portal"
admin.site.index_title = "Bienvenidos a Refugio App"

admin.site.unregister(Token)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(RefugioEvent, RefugioEventAdmin)
admin.site.register(Colaboration, ColaborationAdmin)
admin.site.register(ColaborationColaborators, ColaborationColaboratorsAdmin)
admin.site.register(Timeline, TimelineAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(AnimalSpecie)
admin.site.register(AdoptionRequest, AdoptionRequestAdmin)
