from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    list_filter = ('author', 'publication_year')  # Sidebar filters
    search_fields = ('title', 'author')  # Search bar


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo',)
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('date_of_birth', 'profile_photo',)
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
