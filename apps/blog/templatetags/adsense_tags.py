from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.filter
def inject_adsense_after_n_paragraph(value, arg):
    ad_code = render_to_string('blog/adsense.html')
    paragraphs = value.split('</p>')

    if arg < len(paragraphs):
        paragraphs[arg] = ad_code + paragraphs[arg]

    value = '</p>'.join(paragraphs)
    return value
