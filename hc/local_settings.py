DATABASES = {
    'default': {
        'ENGINE':   'django.db.backends.postgresql',
        'NAME':     'hc',
        'USER':     'ahmedyusuf',
        'PASSWORD': '',
        'TEST': {'CHARSET': 'UTF8'}
    }
}


DJMAIL_REAL_BACKEND = 'django_ses_backend.SESBackend'
AWS_SES_ACCESS_KEY_ID = "put-access-key-here"
AWS_SES_SECRET_ACCESS_KEY = "put-secret-access-key-here"
AWS_SES_REGION_NAME = 'us-east-1'
AWS_SES_REGION_ENDPOINT = 'email.us-east-1.amazonaws.com'
