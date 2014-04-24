#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'CommonQ'
SITENAME = u"CommonQ's Blog"
SITEURL ='http://commonq.github.io'
SITE_SOURCE = u"https://github.com/CommonQ/commonq.github.io"
SITE_TAGLINE = u"木秀于林"

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh'
ARCHIVES_URL = "archives.html"
GITHUB_URL = u"https://github.com/CommonQ/commonq.github.io"
GITHUB_POSITION = "left"





#FEED_DOMAIN = SITEURL
#FEED_ATOM = None
#FEED_ALL_ATOM = u"feeds/all.atom.xml"

THEME = "gum" 






DISPLAY_PAGES_ON_MENU = False

DISPLAY_PAGES_ON_RIGHT = True





# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('Github','https://github.com/CommonQ'),('新浪微博', 'http://weibo.com/u/1239942131'),)

DEFAULT_PAGINATION = 10



EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/bdsitemap.txt": {"path": "bdsitemap.txt"},
    "extra/googledbee14f7be5461f0.html": {"path": "googledbee14f7be5461f0.html"},
    "extra/404.html": {"path": "404.html"},
}



PLUGIN_PATH = [u'pelican-plugins']  # 设置插件路径
PLUGINS = ['sitemap']


DISQUS_SITENAME = u"commonq"  # 设置disque评论插件的帐号

# 配置sitemap 插件
# 配置sitemap 插件
SITEMAP = {
     "format": "xml",
     "priorities": {
         "articles": 0.7,
         "indexes": 0.5,
         "pages": 0.3,
     },
 "changefreqs": {
     "articles": "monthly",
     "indexes": "daily",
     "pages": "monthly",
     }
 }



STATIC_PATHS = [u"static/upload",
		u"static/img",
		"images",
                "extra/bdsitemap.txt",
                "extra/google5b5f348354004b46.html",
                "extra/404.html",
                ]



#KEYWORDS = u"Python, Linux, vim, 开源"

GOOGLE_ANALYTICS =  u"UA-50304302-1"

# Uncomment followig line if you want document-relative URLs when deve#RELATIVE_URLS = True
