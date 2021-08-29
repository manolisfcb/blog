from django.contrib import admin

# Register your models here.

from .models import Post,PostView, Comments,Like,DisLike, User
admin.site.register(User)
admin.site.register(Post)
admin.site.register(PostView)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(DisLike)