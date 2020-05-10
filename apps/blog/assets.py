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

js = Bundle(
    os.path.join('js', 'jquery-3.2.1.min.js'),
    os.path.join('js', 'highlight.min.js'),
    os.path.join('js', 'bootstrap.min.js'),
    filters='jsmin', output='js/build.js'
)
register('css_all', css)
register('js_all', js)
