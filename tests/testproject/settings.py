import os
import sys
from pathlib import Path

DEBUG = True
SECRET_KEY = "thisisnotneeded"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "securepasswords",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "securepasswords.middleware.SecurePasswordMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "securepasswords",
    }
}

SITE_ID = 1

MEDIA_URL = "/media/"
STATIC_URL = "/static/"

ROOT_URLCONF = "tests.testproject.urls"


# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

LOGGING = {
    "version": 1,
    "disable_existing_loggers": True,
    "formatters": {"console": {"format": "%(asctime)s %(levelname)-8s %(name)-12s %(message)s"}},
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "console",
            "stream": sys.stdout,
        },
    },
    "root": {"handlers": ["console"], "level": "INFO"},
    "loggers": {
        "securepasswords": {
            "handlers": ["console"],
            "level": os.getenv("SECUREPASSWORDS_LOG_LEVEL", "INFO"),
            "propagate": False,
        },
    },
}

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    #     'OPTIONS': {
    #         'min_length': 9,
    #     }
    # },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
    {
        "NAME": "securepasswords.validators.HistoryValidator",
    },
    {
        "NAME": "securepasswords.validators.RepeatedCharValidator",
    },
    {
        "NAME": "securepasswords.validators.ArithmeticSequenceValidator",
    },
]

SECURE_PASSWORDS = {
    "MAX_PASSWORD_AGE": 1,  # days
    "PASSWORD_HISTORY_LENGTH": 2,  # do not reuse the last n passwords
    # "CHANGE_PASSWORD_URL": ("password_change", str),  # override may be view name or URL
}

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
LOGIN_URL = "admin:login"
