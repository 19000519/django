from django.contrib import admin
from .models import Video, Comment

# Register your models here.
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'datetime','user')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('video', 'datetime','user', 'text')

admin.site.register(Video,VideoAdmin)
admin.site.register(Comment, CommentAdmin)