from django.contrib import admin
from profiles_api import models

@admin.register(models.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(models.ProfileFeedItem)
class ProfileFeedItemAdmin(admin.ModelAdmin):
    pass