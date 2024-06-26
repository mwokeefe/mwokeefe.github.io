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
PAGE_PATHS = ["pages"]
ARTICLE_PATHS = ["tech", "papers"]
STATIC_PATHS = ["images"]
USE_FOLDER_AS_CATEGORY = True

# URL settings for articles
ARTICLE_URL = "{slug}.html"
ARTICLE_SAVE_AS = "{slug}.html"

# URL settings for pages
PAGE_URL = "pages/{slug}.html"
PAGE_SAVE_AS = "pages/{slug}.html"
