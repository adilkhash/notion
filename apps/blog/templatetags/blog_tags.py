from django.template.defaulttags import register
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

from apps.blog.utils import get_latest_jobs


@register.filter
def text_preview(text):
    more = text.find('<!--more-->')
    if more != -1:
        return text[:more]
    else:
        return text


@register.filter
def erase_breaks(text):
    return text.replace('\n', '').replace('\r\n', '').replace('\r', '')


@register.simple_tag
def display_jobs(limit=5):
    jobs = get_latest_jobs(limit)
    return mark_safe(render_to_string('tags/jobs.html', {'jobs': jobs}))
