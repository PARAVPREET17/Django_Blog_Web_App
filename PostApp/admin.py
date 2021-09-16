from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display =('title','author','date_posted','category','is_published')
    list_display_links=('title','author')
    list_order_by = ('-date_posted',)
    list_filter = ('category',)
    list_editable=('is_published',)
# Register your models here.
admin.site.register(Post,PostAdmin)