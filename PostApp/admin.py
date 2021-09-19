from django.contrib import admin
from .models import Post
# from django_summernote.admin import SummernoteModelAdmin



class PostAdmin(admin.ModelAdmin):
    list_display =('title','author','date_posted','category','is_published')
    list_display_links=('title','author')
    list_order_by = ('-date_posted',)
    list_filter = ('category',)
    list_editable=('is_published',)
    # summernote_fields = ('content',)
    prepopulated_fields={'category_slug':('category',)}
# Register your models here.
admin.site.register(Post,PostAdmin)