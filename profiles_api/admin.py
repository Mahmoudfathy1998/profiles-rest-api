from django.contrib import admin

from profiles_api import models

# Registers the userProfile model in the admin site to makes it visible in the admin interface
admin.site.register(models.UserProfile)