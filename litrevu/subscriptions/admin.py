from django.contrib import admin
from .models import UserFollows


class UserFollowsAdmin(admin.ModelAdmin):
    model = UserFollows
    verbose_name_plural = "User Follows"


admin.site.register(UserFollows, UserFollowsAdmin)
