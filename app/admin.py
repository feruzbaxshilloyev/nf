from .models import Category, News, Sponsors, ContactMessage
from django.contrib import admin


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "view", "created_at")
    list_filter = ("view", )
    search_fields = ("name", "email")


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Sponsors)
