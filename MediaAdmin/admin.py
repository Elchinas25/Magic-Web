from django.contrib import admin

from modeltranslation.admin import TranslationAdmin, TranslationTabularInline

from .models import VideoAdmin, SliderAdmin, SliderImage, Video, Style, DigonalStyle


class SliderImageInline(TranslationTabularInline):
	model = SliderImage

class AdminSliderImage(admin.ModelAdmin):
	inlines = [SliderImageInline,]

admin.site.register(SliderAdmin, AdminSliderImage)


class VideoInline(TranslationTabularInline):
	model = Video

class UserVideoAdmin(admin.ModelAdmin):
	inlines = [VideoInline,]

admin.site.register(VideoAdmin, UserVideoAdmin)
admin.site.register(Style)

class DigonalStyleAdmin(TranslationAdmin):
	pass

admin.site.register(DigonalStyle, DigonalStyleAdmin)




