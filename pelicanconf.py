#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Juan BC'
SITENAME = 'JBC Personal Webpage'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Argentina/Cordoba'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
STATIC_PATHS = ['images', 'pdfs', 'pages/images']


DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/elegant'

OUTPUT_PATH = 'output/'

SHOW_DRAFTS = os.getenv("SHOW_DRAFTS", None) == "True"
print(SHOW_DRAFTS)

if not SHOW_DRAFTS:
    DEFAULT_METADATA = {
        'status': 'draft',
    }
