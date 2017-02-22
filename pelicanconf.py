#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Bulk Eats'
SITENAME = u'Bulk Eats'
SITEURL = 'https://bulkeats.com'

TIMEZONE = 'GMT'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Example', 'example'),
        )

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/bulkeats'),
          )


DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PAGE_PATHS = ['content/pages']

# Theme
THEME = "themes/pelican-themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "flatly"
#DISPLAY_ARTICLE_INFO_ON_INDEX = True

# Code block theme
PYGMENTS_STYLE = 'solarizeddark'

# Custom css
CUSTOM_CSS = 'static/custom.css'
STATIC_PATHS = ['images', 'extra/custom.css']

EXTRA_PATH_METADATA = {
        'extra/custom.css': {'path': 'static/custom.css'}
        }

# Other
PLUGINS = ['minification']
READERS = {'html': None}
IGNORE_FILES = ['README.rst', 'LISEZ-MOI.rst']
HIDE_SIDEBAR = True
