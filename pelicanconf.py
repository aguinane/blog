#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Default Settings
AUTHOR = 'Alex Guinane'
COPYRIGHT_NAME = AUTHOR
SITENAME = 'Alex Guinane'
SITETITLE = SITENAME
SITESUBTITLE = 'The blog formerly known as [Tales From Turgi]'
SITELOGO = '/images/avatar.jpg'
FAVICON = '/images/favicon.ico'
TIMEZONE = 'Australia/Brisbane'
DEFAULT_DATE_FORMAT = ('%d %b %Y')
DEFAULT_LANG = 'en'

# Output paths
PATH = 'content'
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}


# Theme Settings
THEME = 'themes/Flex'

# Blogroll
MAIN_MENU = False
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = ()
LINKS = (('Blog', '/blog.html'),
         ('Archives', '/archives.html'),
         ('Categories', '/categories.html'),
         ('Tags', '/tags.html'),
         )
INDEX_SAVE_AS = "blog.html"
ARTICLE_URL = 'posts/{date:%Y}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{slug}/index.html'
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

# Social widget
GITHUB_URL = "https://github.com/aguinane"
TWITTER_USERNAME = "alexguinane"
SOCIAL = (
    ("twitter", 'https://twitter.com/alexguinane'),
    ("github", 'https://github.com/aguinane'),
    ("linkedin", 'https://www.linkedin.com/in/alexguinane/'),
    ("rss", '/feeds/all.rss.xml'),
)


# Feed generation is usually not desired when developing
SUMMARY_MAX_LENGTH = 25
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = 10
