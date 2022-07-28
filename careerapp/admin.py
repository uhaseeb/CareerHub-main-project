from django.contrib import admin
from .models import Feature,Post, User
from django.contrib.auth.admin import UserAdmin

admin.site.register(Feature)
admin.site.register(Post)
admin.site.register(User)
