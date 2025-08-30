from .base import *

print("""
================================================================
==================            PROD            ==================
================================================================
""")

DEBUG = False

# AWS 관련 설정 ###########################################
AWS_ACCESS_KEY_ID       = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY   = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_REGION_NAME      = 'ap-northeast-2'  # 서울 리전
AWS_S3_CUSTOM_DOMAIN    = f'{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_S3_REGION_NAME}.amazonaws.com'
AWS_S3_FILE_OVERWRITE   = True
AWS_QUERYSTRING_AUTH    = False

INSTALLED_APPS += ['storages']

STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/static/'

# django 4.2 버전 이상에서 동작
STORAGES = {
    "default": {
        # "BACKEND": "storages.backends.s3.S3Storage",
        "BACKEND": "vogue_me.settings.storages.MediaStorage",
    },
    "staticfiles": {
        # "BACKEND": "storages.backends.s3.S3Storage",
        "BACKEND": "vogue_me.settings.storages.StaticStorage",
    }
}
# django 4.2 버전 미만에서만 동작.
# DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
# STATICFILES_STORAGE  = "storages.backends.s3boto3.S3Boto3Storage"