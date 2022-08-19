from modeltranslation.translator import TranslationOptions, register
from .models import ContactUs


@register(ContactUs)
class ContactTranslationOptions(TranslationOptions):
    fields = ('address', 'working_hours')