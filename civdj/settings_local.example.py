import os
import secrets

# BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = '/opt/civ4/data'

SECRET_KEY = secrets.token_hex(nbytes=50)
DEBUG = True
ALLOWED_HOSTS = ["*"]

# Add new languages here and create with 
# 'python3 manage.py makemessages --locale {your language code}'
# translation file in civdj/pbspy/locale/...
LANGUAGES = (
    ("en", ("English")),
    ("de", ("Deutsch")),
)

# Permanent storage of static files
if not DEBUG:
    # Set STATIC_ROOT permissions such that
    #      manage.py [collectstatic|compilestatic]
    # can write the files.
    STATIC_ROOT = '/var/www/html/pbspy/static/'
    STATIC_URL = 'http://localhost/pbspy/static/'

BASE_URL = 'https://localhost'

# Look into django docs for setup
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
