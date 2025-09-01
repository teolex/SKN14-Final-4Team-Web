import os

# DJANGO_SETTINGS_MODULE이 없으면 기본값을 development로
env = os.getenv('DJANGO_ENV', 'development')

if env == 'production':    from .production import *
elif env == "migrater":    from .migrater   import *
else:                      from .base       import *
