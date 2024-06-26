#!/usr/bin/env python
# -*- coding: utf-8 -*- #


AUTHOR = "mwokeefe"
SITENAME = "Test"
SITEURL = ""

TIMEZONE = "GMT"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
THEME = "themes/Flex/"

ARTICLE_ORDER_BY = "attribute"
PAGE_ORDER_BY = "attribute"

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
PATH = "content"
STATIC_PATHS = ["tech"]
ARTICLE_PATHS = STATIC_PATHS
USE_FOLDER_AS_CATEGORY = True

ARTICLE_URL = "{slug}/"
ARTICLE_SAVE_AS = "{slug}/index.html"
PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"
