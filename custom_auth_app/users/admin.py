from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.
#User = settings.AUTH_USER_MODEL 

class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email','password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name','phone')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email','first_name','last_name','phone','password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name','phone', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name','email','phone',)
    ordering = ('email','phone',)


admin.site.register(get_user_model(),CustomUserAdmin)