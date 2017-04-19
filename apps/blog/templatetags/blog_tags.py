from django.template.defaulttags import register


@register.filter
def text_preview(text):
    more = text.find('<!--more-->')
    if more != -1:
        return text[:more]
    else:
        return text
