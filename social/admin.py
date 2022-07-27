from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User, Profile, Post


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User
    # fields = ["username"] 
    inlines = [ProfileInline]
    prepopulated_fields = {"slug": ("username",)}


admin.site.unregister(Group)
# admin.site.register(Profile)
admin.site.register(Post)
