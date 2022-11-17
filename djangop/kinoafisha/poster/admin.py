from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

# Login root
# Password root

class PosterAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'get_html_photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published',)
    prepopulated_fields = {"slug": ("title",)}

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Фото'
    


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Poster, PosterAdmin,)
admin.site.register(Category, CategoryAdmin,)

admin.site.site_title = 'Админ-панель сайта "Киноафиша"'
admin.site.site_header = 'Админ-панель сайта "Киноафиша"'
