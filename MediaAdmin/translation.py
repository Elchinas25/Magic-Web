from modeltranslation.translator import translator, TranslationOptions

from .models import SliderImage, Video, DigonalStyle


class SliderImageTranslationOptions(TranslationOptions):
    fields = ('text',)

translator.register(SliderImage, SliderImageTranslationOptions)

class VideoTranslationOptions(TranslationOptions):
    fields = ()

translator.register(Video, VideoTranslationOptions)

class DigonalStyleTranslationOptions(TranslationOptions):
    fields = ('statement', 'second_sec_text', 'third_sec_text', 'fourth_sec_text', 'second_sec_title', 'third_sec_title', 'fourth_sec_title', )

translator.register(DigonalStyle, DigonalStyleTranslationOptions)