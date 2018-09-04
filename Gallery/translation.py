from modeltranslation.translator import translator, TranslationOptions
from .models import Event

class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

translator.register(Event, EventTranslationOptions)