from .base import *
from .secure import *
from .packages import *
from decouple import config

ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(',')])

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config("DB_NAME"),
        "USER": config("DB_USER"),
        "PASSWORD": config("DB_PASSWORD"),
        "HOST": config("DB_HOST"),
        "PORT": config("DB_PORT", cast=int)
    }
}


# Arvan Cloud Storage

DEFAULT_FILE_STORAGE = config("DEFAULT_FILE_STORAGE")
AWS_S3_ACCESS_KEY_ID = config("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = config("AWS_S3_SECRET_ACCESS_KEY")
AWS_S3_ENDPOINT_URL = config("AWS_S3_ENDPOINT_URL")
AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
AWS_SERVICE_NAME = config("AWS_SERVICE_NAME")
AWS_S3_FILE_OVERWRITE = config("AWS_S3_FILE_OVERWRITE", cast=bool)  # two file same name do replace?
AWS_LOCAL_STORAGE = f'{BASE_DIR}/aws/'

# zarinpal
MERCHANT = "00000000-0000-0000-0000-000000000000"
SANDBOX = True