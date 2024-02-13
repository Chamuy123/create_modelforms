from django.contrib import admin

# Register your models here.
from app.models import *

class customatizeWebpage(admin.ModelAdmin):
    list_display=['tname','name','url','email']
    list_display_links=['name']
    list_filter=['tname']
    search_fields=('name',)
    list_editable=('email',)
    list_per_page=1

admin.site.register(Topic)
admin.site.register(Webpage,customatizeWebpage)
admin.site.register(Accessrecord)