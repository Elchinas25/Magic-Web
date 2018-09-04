# from django.contrib import admin

# from .models import Event, Image, GalleryStyleAdmin

# class ImageInline(admin.TabularInline):
# 	model = Image

# class EventAdmin(admin.ModelAdmin):
# 	inlines = [ImageInline]

# admin.site.register(Event, EventAdmin)
# admin.site.register(GalleryStyleAdmin)




from django.contrib import admin
from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import Event, Image, GalleryStyleAdmin

# class ImageInline(TranslationTabularInline):
#     model = Image

class ImageInline(admin.TabularInline):
	model = Image


class EventAdmin(TranslationAdmin):
    inlines = [ImageInline,]

admin.site.register(Event, EventAdmin)
admin.site.register(GalleryStyleAdmin)




