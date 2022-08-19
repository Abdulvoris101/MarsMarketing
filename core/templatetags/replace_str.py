from django import template

register = template.Library()

@register.filter
def to_and(value):
    value = str(value)
    return value

@register.filter
def to_uzb(value):
    value = str(value)
    val = value.split('/')

    if 'en' in val:
        return value.replace('en', 'uz')
    elif 'ru' in val:
        return value.replace('ru', 'uz')
    
    return value

@register.filter
def to_eng(value):
    value = str(value)
    val = value.split('/')

    if 'uz' in val:
        return value.replace('uz', 'en')
    elif 'ru' in val:
        return value.replace('ru', 'en')
    
    return value

@register.filter
def to_rus(value):
    value = str(value)
    val = value.split('/')

    if 'en' in val:
        return value.replace('en', 'ru')
    elif 'uz' in val:
        return value.replace('uz', 'ru')
    
    return value