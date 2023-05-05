from django import template
import re

register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):
    bad_words = ['редиска']
    res = value

    for word in bad_words:
        word = r'\b%s\b' % word  # Apply word boundaries to the bad word
        regex = re.compile(word, re.IGNORECASE)
        res = regex.sub("*" * (len(word) - 4), res)

    return res