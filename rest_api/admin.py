from django.contrib import admin
from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.admin.widgets import AdminFileWidget
from rest_api.models.animals import Animal, ImageAnimal
from rest_api.models.profile import Profile
from django.contrib.auth.models import User, Permission
from django.contrib.auth.admin import UserAdmin
from django_admin_listfilter_dropdown.filters import DropdownFilter


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

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super(CustomUserAdmin, self).get_readonly_fields(request, obj)
        else:
            return 'date_joined', 'username', 'email', 'is_staff', 'is_superuser'

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


admin.site.site_header = "Refugio App Backoffice"
admin.site.site_title = "Backoffice Portal"
admin.site.index_title = "Bienvenidos a Refugio App"

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Permission)
admin.site.register(Animal, AnimalAdmin)