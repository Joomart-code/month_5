from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, ConfirmCode


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    
    ordering=('id',)
    
    list_display = (
        'id',
        'email',
        'phone_number',
        'is_active',
        'is_staff',
        'is_superuser',
        
    )
    
    search_fields = (
        'email',
        'phone_number',
    )
    
    fieldsets=(
        (None,{
            'fields':(
                'email',
                'password',
            )
        }),
        ('Personal info',{
            'fields':(
                'phone_number',
            )
        }),
        ('Permissions',{
            'fields':(
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            )
        }),
    )
    add_fieldsets = (
            (None,{
                'classes': ('wide',),
                'fields':(
                    'email',
                    'phone_number',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_superuser',
                    'is_active',
                ),
            }),
            
        )
@admin.register(ConfirmCode)
class ConfirmCodeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'code',
    )
    search_fields = (
        'user__email',
        'code',
    )