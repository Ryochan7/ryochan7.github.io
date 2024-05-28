AUTHOR = 'Ryochan7'
SITENAME = "Ryochan's Asylum"
SITETITLE = SITENAME
SITEURL = ""
SITELOGO = "/images/5-talim-revealed-soul-calibur-6-new-gameplay-trailert.png"

COPYRIGHT_YEAR = "2024"
COPYRIGHT_NAME = "Ryochan7"

PATH = "content"

TIMEZONE = 'UTC'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = "posts.atom"
#FEED_ALL_ATOM = "feeds/all.atom.xml"
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
#CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
#TAG_FEED_ATOM = "posts/tag/{slug}.atom"
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
"""LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)
"""
LINKS = (
  ("Posts", "/posts/"),
)

EXTERNAL_LINKS = (
  ("Chocolate Pudding", "https://www.youtube.com/watch?v=5OJS9N0ib_Q"),
)

# Social widget
SOCIAL = (
    ("github", "https://github.com/Ryochan7/"),
)

DEFAULT_PAGINATION = 20

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Settings for the URLs of the blog and the articles
ARTICLE_PATHS = ["posts"]
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html"

INDEX_SAVE_AS = "posts/index.html"

YEAR_ARCHIVE_SAVE_AS = "posts/{date:%Y}/index.html"
YEAR_ARCHIVE_URL = "posts/{date:%Y}/"

PAGE_URL = "{slug}/"
PAGE_SAVE_AS = "{slug}/index.html"

#DIRECT_TEMPLATES = ['index']
THEME = "theme/Flex"
DISABLE_URL_HASH = True
MAIN_MENU = True

MENUITEMS = (
  ("Archives", "/archives.html"),
  ("Categories", "/categories.html"),
  ("Tags", "/tags.html"),
)

STATIC_PATHS = ['images', 'extra/favicon.png']
EXTRA_PATH_METADATA = {
    'extra/favicon.png': {'path': 'favicon.png'}
}
