import os

from django_assets import Bundle, register

css = Bundle(
    os.path.join('css', 'normalize.css'),
    os.path.join('css', 'bootstrap.min.css'),
    os.path.join('css', 'bootstrap-theme.min.css'),
    os.path.join('css', 'style.css'),
    os.path.join('css', 'monokai-sublime.min.css'),
    filters='cssmin', output='css/build.css'
)
register('css_all', css)
