from django.contrib import admin
from . models import *



# Register your models here.

class catadmin(admin.ModelAdmin):
    list_display=['name','slug']
    list_editable=['slug']
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)

class prodAdmin(admin.ModelAdmin):
    list_display=['name','slug','price','stock','img']
    list_editable=['price','stock','img']
    prepopulated_fields={'slug':('name',)}
admin.site.register(product,prodAdmin)