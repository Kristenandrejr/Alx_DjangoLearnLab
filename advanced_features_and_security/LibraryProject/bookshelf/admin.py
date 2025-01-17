from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, Permission
from .models import CustomUser, Book

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "date_of_birth", "profile_photo")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "username", "password1", "password2", "date_of_birth", "profile_photo"),
        }),
    )
    list_display = ("email", "username", "is_staff", "date_of_birth")
    search_fields = ("email", "username")
    ordering = ("email",)

admin.site.register(CustomUser, CustomUserAdmin)

# Register the Book model
admin.site.register(Book)

# Create and assign permissions to groups in the Django admin interface
def create_groups_and_permissions():
    group_editors, created = Group.objects.get_or_create(name='Editors')
    group_viewers, created = Group.objects.get_or_create(name='Viewers')
    group_admins, created = Group.objects.get_or_create(name='Admins')

    # Permissions for Editors
    can_edit = Permission.objects.get(codename='can_edit')
    can_create = Permission.objects.get(codename='can_create')
    group_editors.permissions.set([can_edit, can_create])

    # Permissions for Viewers
    can_view = Permission.objects.get(codename='can_view')
    group_viewers.permissions.set([can_view])

    # Permissions for Admins
    can_delete = Permission.objects.get(codename='can_delete')
    group_admins.permissions.set([can_view, can_create, can_edit, can_delete])

create_groups_and_permissions()
