#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Sarita Singh'

HIDE_AUTHORS = True
# SITENAME = 'Integrating ScanCode Toolkit to FOSSology'
SITEURL = 'https://itssingh.github.io/gsoc-blog'
NEST_CSS_MINIFY = False
SITETITLE = 'GSoC 2021'
THEME = 'themes/nest'

NEST_INDEX_HEAD_TITLE = u'GSoC Blog'  # bar title
NEST_INDEX_HEADER_TITLE = u'Integrating ScanCode Toolkit to FOSSology'  # header text
NEST_INDEX_HEADER_SUBTITLE = u'Post by Sarita Singh'  # sub header
NEST_INDEX_CONTENT_TITLE = u'Posts'  # Article header

PATH = 'content'


TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

MENUITEMS = [('HOMEPAGE', 'index.html'), ('CATEGORY', 'categories.html'), ('TAG', 'tags.html')]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

NEST_SOCIAL_COLUMN_TITLE = u'Social'
NEST_LINKS_COLUMN_TITLE = u'Links'

NEST_SITEMAP_COLUMN_TITLE = u'Sitemap'
NEST_SITEMAP_MENU = [('Archives', '/archives.html'), ('Authors','/authors.html')]

# Blogroll
SOCIAL = (('GitHub', 'https://github.com/itssingh/'),
         ('LinkedIn', 'https://www.linkedin.com/in/s-sarita/'), )

# Social widget
LINKS = (('FOSSology', 'https://github.com/fossology/fossology'),('ScanCode', 'https://github.com/nexB/scancode-toolkit'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']


# archives.html
NEST_ARCHIVES_HEAD_TITLE = u'Archives'
NEST_ARCHIVES_HEAD_DESCRIPTION = u'Posts Archives'
NEST_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_ARCHIVES_HEADER_SUBTITLE = u'Archives for all posts'
NEST_ARCHIVES_CONTENT_TITLE = u'Archives'
# article.html
NEST_ARTICLE_HEADER_BY = u'By'
NEST_ARTICLE_HEADER_MODIFIED = u'modified'
NEST_ARTICLE_HEADER_IN = u'in category'
# author.html
NEST_AUTHOR_HEAD_TITLE = u'Posts by'
NEST_AUTHOR_HEAD_DESCRIPTION = u'Posts by'
NEST_AUTHOR_HEADER_SUBTITLE = u'Posts archives'
NEST_AUTHOR_CONTENT_TITLE = u'Posts'
# authors.html
NEST_AUTHORS_HEAD_TITLE = u'Author list'
NEST_AUTHORS_HEAD_DESCRIPTION = u'Author list'
NEST_AUTHORS_HEADER_TITLE = u'Author list'
NEST_AUTHORS_HEADER_SUBTITLE = u'Archives listed by author'
# categories.html
NEST_CATEGORIES_HEAD_TITLE = u'Categories'
NEST_CATEGORIES_HEAD_DESCRIPTION = u'Archives listed by category'
NEST_CATEGORIES_HEADER_TITLE = u'Categories'
NEST_CATEGORIES_HEADER_SUBTITLE = u'Archives listed by category'
# category.html
NEST_CATEGORY_HEAD_TITLE = u'Category Archive'
NEST_CATEGORY_HEAD_DESCRIPTION = u'Category Archive'
NEST_CATEGORY_HEADER_TITLE = u'Category'
NEST_CATEGORY_HEADER_SUBTITLE = u'Category Archive'
# pagination.html
NEST_PAGINATION_PREVIOUS = u'Previous'
NEST_PAGINATION_NEXT = u'Next'
# period_archives.html
NEST_PERIOD_ARCHIVES_HEAD_TITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_HEAD_DESCRIPTION = u'Archives for'
NEST_PERIOD_ARCHIVES_HEADER_TITLE = u'Archives'
NEST_PERIOD_ARCHIVES_HEADER_SUBTITLE = u'Archives for'
NEST_PERIOD_ARCHIVES_CONTENT_TITLE = u'Archives for'
# tag.html
NEST_TAG_HEAD_TITLE = u'Tag archives'
NEST_TAG_HEAD_DESCRIPTION = u'Tag archives'
NEST_TAG_HEADER_TITLE = u'Tag'
NEST_TAG_HEADER_SUBTITLE = u'Tag archives'
# tags.html
NEST_TAGS_HEAD_TITLE = u'Tags'
NEST_TAGS_HEAD_DESCRIPTION = u'Tags List'
NEST_TAGS_HEADER_TITLE = u'Tags'
NEST_TAGS_HEADER_SUBTITLE = u'Tags List'
NEST_TAGS_CONTENT_TITLE = u'Tags List'
NEST_TAGS_CONTENT_LIST = u'tagged'
