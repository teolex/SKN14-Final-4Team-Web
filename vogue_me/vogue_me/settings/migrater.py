from .base import *
import os

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # or 'mysql', 'sqlite3', 'oracle'
        'NAME': '20250901_looplabel',
        'USER': 'migrater',
        'PASSWORD': os.getenv("DB_MIGRATER_PASSWORD"),
        'HOST': 'database-1.c386wgw8g00f.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}