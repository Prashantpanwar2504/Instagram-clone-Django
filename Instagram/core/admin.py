from django.contrib import admin
from core.models import  (
    Post,
    Comment,
    Like,
    Follow,
)
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
    model = Post  # model we want to use
    list_display = ('text', 'image', 'user', 'posted_on', 'updated_on')


admin.site.register(Post, PostModelAdmin)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(Follow)