from django.contrib import admin
from .models import User, Followers, FriendSolicitations

# Register your models here.
admin.site.register(User)
admin.site.register(Followers)
admin.site.register(FriendSolicitations)
