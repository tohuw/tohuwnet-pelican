#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

SITEURL = 'https://tohuw.net'
SITENAME = u'Tohuw.Net'

DEFAULT_LANG = u'en'
LOCALE = ( 'en_US.utf8', )
DEFAULT_DATE_FORMAT = '%B %d, %Y'
# DATE_FORMATS = { 'en': '%a, %d %b %Y', }
TIMEZONE = 'America/New_York'
DEFAULT_DATE = None

PATH = 'content'
THEME = 'themes/qalal'
# JINJA_EXTENSIONS = []
# JINJA_FILTERS = {}
PLUGIN_PATHS = ['plugins']
PLUGINS = ['tipue_search', 'pelican_comment_system']
# MD_EXTENSIONS = ['codehilite(css_class=highlight)','extra']
# PYGMENTS_RST_OPTIONS = []
TYPOGRIFY = True

OUTPUT_PATH = 'output/'
DELETE_OUTPUT_DIRECTORY = False
WRITE_SELECTED = []
# OUTPUT_RETENTION = ( ".git", )
OUTPUT_SOURCES = False
OUTPUT_SOURCES_EXTENSION = '.text'
IGNORE_FILES = ['.*', '*.cod']
# LOG_FILTER = [(logging.WARN, 'Feeds generated without SITEURL set properly may not be valid')]

CACHE_PATH = 'cache'
CACHE_CONTENT = False
LOAD_CONTENT_CACHE = True
AUTORELOAD_IGNORE_CACHE = True
CHECK_MODIFIED_METHOD = 'md5'
CONTENT_CACHING_LAYER = 'reader'
GZIP_CACHE = True

TITLE = 'Tohuw.Net'
AUTHOR = u'Ron Scott-Adams'
SITESUBTITLE = 'Elucidating Systems Architecture, Operations, & Yak Shaving'
# DEFAULT_METADATA = ()

DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'authors', 'search'))
# PAGINATED_DIRECT_TEMPLATES = ('index',)
# TEMPLATE_PAGES = {'extras/search.html': 'search.html'}
EXTRA_TEMPLATES_PATHS = []
ARTICLE_EXCLUDES = ['extras']
PAGE_EXCLUDES = ['extras']
STATIC_PATHS = [
        'extras',
        'images',
        'comments',
        'cgi-bin'
]
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'
PATH_METADATA = ''
EXTRA_PATH_METADATA = { 'extras/robots.txt': {'path': 'robots.txt'}, }
SLUGIFY_SOURCE = 'title'

# INTRASITE_LINK_REGEX = '[{|](?P<what>.*?)[|}]'
RELATIVE_URLS = False

MENUITEMS = ( ('Topics', '/topics.html'), ('Archives','/archives/'), ('Ron Scott-Adams', '/ron-scott-adams.html') ,)
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

SUMMARY_MAX_LENGTH = 50

FEED_DOMAIN = SITEURL
#FEED_MAX_ITEMS =

FEED_ALL_ATOM = 'feeds/all.atom.xml'
FEED_ATOM = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
TAG_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

FEED_ALL_RSS = None
FEED_RSS = None
CATEGORY_FEED_RSS = None
TAG_FEED_RSS = None
AUTHOR_FEED_RSS = None
TRANSLATION_FEED_RSS = None

SLUG_SUBSTITUTIONS = [('and', '')]

ARTICLE_URL = 'articles/{slug}'
ARTICLE_SAVE_AS = 'articles/{slug}.html'

ARCHIVES_SAVE_AS = 'archives/index.html'
YEAR_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'archives/{date:%Y}/{date:%b}/index.html'
DAY_ARCHIVE_SAVE_AS = ''
NEWEST_FIRST_ARCHIVES = True

DRAFT_URL = 'drafts/{slug}.html'
DRAFT_SAVE_AS = 'drafts/{slug}.html'
WITH_FUTURE_DATES = False

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

CATEGORIES_SAVE_AS = 'topics.html'
CATEGORY_URL = 'topic/{slug}.html'
CATEGORY_SAVE_AS = 'topic/{slug}.html'
USE_FOLDER_AS_CATEGORY = False
DEFAULT_CATEGORY = 'misc'
REVERSE_CATEGORY_ORDER = False

TAGS_SAVE_AS = 'tags.html'
TAG_URL = 'tag/{slug}.html'
TAG_SAVE_AS = 'tag/{slug}.html'
TAG_CLOUD_STEPS = 5
TAG_CLOUD_MAX_ITEMS = 100

AUTHORS_SAVE_AS = 'authors.html'
AUTHOR_URL = 'author/{slug}.html'
AUTHOR_SAVE_AS = 'author/{slug}.html'

## Comments
# DISQUS_SITENAME = 'tohuw'

## Analytics
#GOOGLE_ANALYTICS =
#GOSQUARED_SITENAME =
PIWIK_URL = 'tohuw.net/stats'
PIWIK_SSL_URL = 'tohuw.net/stats'
PIWIK_SITE_ID = 1

GITHUB_URL = "https://github.com/tohuw"
LINKS = (('<span class="links-name">HighExecutive</span> (Ruminations of my illustrious wife)', 'http://highexecutive.net'),
         ('<span class="links-name">UberMarianne</span> (My sister-in-law introspects)', 'http://ubermarianne.net'),
         ('<span class="links-name">Dadhacker</span> (An old and new school cantankerous coder)', 'http://dadhacker.com'))

SOCIAL = (('<span class="fa-twitter"></span>', 'https://twitter.com/tohuw'),
          ('<span class="fa-linkedin"></span>', 'https://linkedin.com/in/tohuw'),
          ('<span class="fa-github"></span>', GITHUB_URL))

DEFAULT_PAGINATION = False
DEFAULT_ORPHANS = 3
# PAGINATION_PATTERNS = (
#         (1, '{base_name}/', '{base_name}/index.html'),
#         (2, '{base_name}/page/{number}/', '{base_name}/page/{number}/index.html'),
# )

## Plugin-Specific Settings
PELICAN_COMMENT_SYSTEM = False
PELICAN_COMMENT_SYSTEM_DIR = 'comments'
PELICAN_COMMENT_SYSTEM_IDENTICON_OUTPUT_PATH = 'images/avatars'
PELICAN_COMMENT_SYSTEM_IDENTICON_DATA = {'author'}
PELICAN_COMMENT_SYSTEM_IDENTICON_SIZE = 54
PELICAN_COMMENT_SYSTEM_AUTHORS = {
    ('Ron'): "images/avatars/me-at-creek.png",
    ('Tom'): "images/authors/tom.png",
}
PELICAN_COMMENT_SYSTEM_FEED = 'feeds/comment.%s.atom.xml'
COMMENT_URL = '#comment-{slug}'

## Qalal-Specific Settings
ARTICLES_RECENT_TITLE = 'More, Here'
ARTICLES_SHOW_RECENT = True
ARTICLE_SHOW_DATE = True
ARTICLE_SHOW_EDITINFO = True
ARTICLE_SHOW_AUTHORS = True
ARTICLE_SHOW_CATEGORY = True
ARTICLE_SHOW_TAGS = True
ARTICLE_SHOW_SHARE = False
PAGE_SHOW_EDITINFO = True
CUSTOM_AUTHOR_URL = 'ron-scott-adams.html'
LINKS_TITLE = 'More, Elsewhere'
SOCIAL_TITLE = False
FEED_TITLE = '<span class="fa-rss"></span>'
TWITTER_USERNAME = 'tohuw'
TIPUE_SEARCH_ENABLED = 'tipue_search' in PLUGINS
ISSO_ENABLED = True
ISSO_DEFAULT_STYLE = False
ISSO_AVATARS = False
