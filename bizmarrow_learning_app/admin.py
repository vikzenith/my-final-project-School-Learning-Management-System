from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from bizmarrow_learning_app.models import CustomUser


class UserModel(UserAdmin):
    pass


from embed_video.admin import AdminVideoMixin
from .models import *

admin.site.register(CustomUser,UserModel)


class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(VideoStaffs, MyModelAdmin)