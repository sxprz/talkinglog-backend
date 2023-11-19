from django.contrib import admin
from main.models import *
from django.contrib.auth.models import User, Group


# Register your models here.

admin.site.register(Session)

admin.site.register(ChatHistory)

admin.site.register(DefaultCategory)
admin.site.register(DefaultPrompt)


admin.site.unregister(User)
admin.site.unregister(Group)
