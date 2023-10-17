


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-9#w@asdasdasdfsdggdfsh0slmrwm@q!jarer(b8gf=q*kjd1c@b^x*'

DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'helpdesk',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [STATIC_DIR]
