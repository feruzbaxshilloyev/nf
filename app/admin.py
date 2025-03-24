from .models import Category, News, Sponsors, ContactMessage, Comment, Profile
from django.contrib import admin


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'created_at', 'news')
    list_filter = ('created_at', 'author')
    search_fields = ('content', 'author__username')


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "view", "created_at")
    list_filter = ("view",)
    search_fields = ("name", "email")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("avatar", 'phone', 'address', 'birth_date', 'user')


admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Sponsors)
admin.site.register(Profile, ProfileAdmin)
