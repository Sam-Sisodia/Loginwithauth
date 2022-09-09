from django.contrib import admin
from . models import *
from . form import *
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model = User
    add_form = CustomUserProfileForm
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'usertype', 'is_staff', 'is_superuser')

    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'User type',
            {
                'fields':('usertype',)
            }
        )
    )
admin.site.register(User, CustomUserAdmin)
admin.site.register(Course)
admin.site.register(CourseChapter)
admin.site.register(Assignment)