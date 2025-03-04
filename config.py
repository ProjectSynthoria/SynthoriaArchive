import os
import re

DEBUG = False

MAINTENANCE_MODE = False
MAINTENANCE_MODE_MESSAGE = 'Site is currently in read-only maintenance mode.'
MAINTENANCE_MODE_LOGINS = True

RAID_MODE_LIMIT_UPLOADS = True
RAID_MODE_UPLOADS_MESSAGE = 'Anonymous uploads are currently disabled.'

# Require manual activation for newly registered accounts
RAID_MODE_LIMIT_REGISTER = True
# Message prepended to the full error message (account.py)
RAID_MODE_REGISTER_MESSAGE = 'Registration is currently limited.'

SITE_NAME = 'Synthoria Archive'
GLOBAL_SITE_NAME = 'Synthoria Archive'

SITE_FLAVOR = 'nyaa' # 'nyaa' or 'sukebei'
EXTERNAL_URLS = {'fap':'***', 'main':'archive.synthoria.moe'}

# Secret keys for Flask
CSRF_SESSION_KEY = '***'
SECRET_KEY = '***'

# Session cookie configuration
SESSION_COOKIE_NAME = 'synthoria_session'
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Lax'

USE_RECAPTCHA = False
USE_EMAIL_VERIFICATION = False
USE_MYSQL = True
# Show seeds/peers/completions in torrent list/page
ENABLE_SHOW_STATS = True

ALLOW_PASSWORD_RESET = False

# A list of strings or compiled regexes to deny registering emails by.
# Regexes will be .search()'d against emails,
# while strings will be a simple 'string in email.lower()' check.
# Leave empty to disable the blacklist.
EMAIL_BLACKLIST = (
    # Hotmail completely rejects "untrusted" emails,
    # so it's less of a headache to blacklist them as users can't receive the mails anyway.
    # (Hopefully) complete list of Microsoft email domains follows:
    re.compile(r'(?i)@hotmail\.(co|co\.uk|com|de|dk|eu|fr|it|net|org|se)'),
    re.compile(r'(?i)@live\.(co|co.uk|com|de|dk|eu|fr|it|net|org|se|no)'),
    re.compile(r'(?i)@outlook\.(at|be|cl|co|co\.(id|il|nz|th)|com|com\.(ar|au|au|br|gr|pe|tr|vn)|cz|de|de|dk|dk|es|eu|fr|fr|hu|ie|in|it|it|jp|kr|lv|my|org|ph|pt|sa|se|sg|sk)'),
    re.compile(r'(?i)@(msn\.com|passport\.(com|net))'),
    # '@dodgydomain.tk'
)
EMAIL_SERVER_BLACKLIST = (
    # Bad mailserver IPs here (MX server.com -> A mail.server.com > 11.22.33.44)
    # '1.2.3.4', '11.22.33.44'
)


# Recaptcha keys (https://www.google.com/recaptcha)
# RECAPTCHA_PUBLIC_KEY = '***'
# RECAPTCHA_PRIVATE_KEY = '***'

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
if USE_MYSQL:
    SQLALCHEMY_DATABASE_URI = ('mysql://synthuser:synthpass@localhost/synthoria?charset=utf8mb4')
else:
    SQLALCHEMY_DATABASE_URI = (
        'sqlite:///' + os.path.join(BASE_DIR, 'synthoria.db') + '?check_same_thread=False')

###########
## EMAIL ##
###########

# 'smtp' or 'mailgun'
MAIL_BACKEND = 'mailgun'
MAIL_FROM_ADDRESS = 'Sender Name <sender@domain.com>'

# Mailgun settings
MAILGUN_API_BASE = 'https://api.mailgun.net/v3/YOUR_DOMAIN_NAME'
MAILGUN_API_KEY = 'YOUR_API_KEY'

# SMTP settings
SMTP_SERVER = '***'
SMTP_PORT = 587
SMTP_USERNAME = '***'
SMTP_PASSWORD = '***'


# The maximum number of files a torrent can contain
# until the site says "Too many files to display."
MAX_FILES_VIEW = 1000

# Verify uploaded torrents have the given tracker in them?
ENFORCE_MAIN_ANNOUNCE_URL = True
MAIN_ANNOUNCE_URL = 'https://tracker.synthoria.moe:6969/announce'

# Tracker API integration - don't mind this
# TRACKER_API_URL = 'http://127.0.0.1:6881/api'
# TRACKER_API_AUTH = 'topsecret'

#############
## Account ##
#############

# Limit torrent upload rate
RATELIMIT_UPLOADS = True
RATELIMIT_ACCOUNT_AGE = 7 * 24 * 3600
# After uploading MAX_UPLOAD_BURST torrents within UPLOAD_BURST_DURATION,
# the following uploads must be at least UPLOAD_TIMEOUT seconds after the previous upload.
MAX_UPLOAD_BURST = 5
UPLOAD_BURST_DURATION = 45 * 60
UPLOAD_TIMEOUT = 15 * 60

# Torrents uploaded without an account must be at least this big in total (bytes)
# Set to 0 to disable
MINIMUM_ANONYMOUS_TORRENT_SIZE = 1 * 1024 * 1024

# Minimum age for an account not to be served a captcha (seconds)
# Relies on USE_RECAPTCHA. Set to 0 to disable.
ACCOUNT_RECAPTCHA_AGE = 7 * 24 * 3600  # A week

# Seconds after which an IP is allowed to register another account
# (0 disables the limitation)
PER_IP_ACCOUNT_COOLDOWN = 72 * 3600

# Backup original .torrent uploads
BACKUP_TORRENT_FOLDER = 'torrents'

############
## Search ##
############

# How many results should a page contain. Applies to RSS as well.
RESULTS_PER_PAGE = 75

# How many pages we'll return at most
MAX_PAGES = 100

# How long and how many entries to cache for count queries
COUNT_CACHE_SIZE = 256
COUNT_CACHE_DURATION = 30

# Use baked queries for database search
USE_BAKED_SEARCH = False

# Use better searching with ElasticSearch
# See README.MD on setup!
USE_ELASTIC_SEARCH = False
# Highlight matches (for debugging)
ENABLE_ELASTIC_SEARCH_HIGHLIGHT = False

# Max ES search results, do not set over 10000
ES_MAX_SEARCH_RESULT = 1000
# ES index name generally (nyaa or sukebei)
ES_INDEX_NAME = SITE_FLAVOR
# ES hosts
ES_HOSTS = ['localhost:9200']

################
## Commenting ##
################

# Time limit for editing a comment after it has been posted (seconds)
# Set to 0 to disable
EDITING_TIME_LIMIT = 0

# Whether to use Gravatar or just always use the default avatar
# (Useful if run as development instance behind NAT/firewall)
ENABLE_GRAVATAR = False

##########################
## Trusted Requirements ##
##########################

# Minimum number of uploads the user needs to have in order to apply for trusted
TRUSTED_MIN_UPLOADS = 3
# Minimum number of cumulative downloads the user needs to have across their
# torrents in order to apply for trusted
TRUSTED_MIN_DOWNLOADS = 0
# Number of days an applicant needs to wait before re-applying
TRUSTED_REAPPLY_COOLDOWN = 30

###########
## Cache ##
###########

# Interesting types include "simple", "redis" and "uwsgi"
# See https://pythonhosted.org/Flask-Caching/#configuring-flask-caching
CACHE_TYPE = "simple"

# Maximum number of items the cache will store
# Only applies to "simple" and "filesystem" cache types
CACHE_THRESHOLD = 8192

# If you want to use redis, try this
# CACHE_TYPE = "redis"
# CACHE_REDIS_HOST = "127.0.0.1"
# CACHE_KEY_PREFIX = "catcache_"


###############
## Ratelimit ##
###############

# To actually make this work across multiple worker processes, use redis
# RATELIMIT_STORAGE_URL="redis://host:port"
RATELIMIT_KEY_PREFIX="nyaaratelimit_"

# Use this to show the commit hash in the footer (see layout.html)
# COMMIT_HASH="[enter your commit hash here]";