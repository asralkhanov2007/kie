from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Contact)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name','id']
	list_display_links = ['name']	
	list_filter = ['name']
	prepopulated_fields = {"slug": ("name",)}

@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
	list_display = ['title','category','id']
	list_display_link = ['title','id']
	prepopulated_fields = {"slug": ("title",)}

admin.site.register(Ordering)
