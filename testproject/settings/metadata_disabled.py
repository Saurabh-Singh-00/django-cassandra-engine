from cassandra.policies import RoundRobinPolicy

from .base import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    },
    'cassandra': {
        'ENGINE': 'django_cassandra_engine',
        'NAME': 'db',
        'USER': 'cassandra',
        'PASSWORD': 'cassandra',
        'TEST_NAME': 'test_db',
        'HOST': CASSANDRA_HOST,
        'OPTIONS': {
            'replication': {
                'strategy_class': 'SimpleStrategy',
                'replication_factor': 1,
            },
            'connection': {
                'schema_metadata_enabled': False,
                'retry_connect': True,
                'consistency': ConsistencyLevel.ALL,
                'load_balancing_policy': RoundRobinPolicy(),
            },
            'session': {'default_timeout': 15},
        },
    },
}

INSTALLED_APPS = BASE_APPS + ['app', 'common', 'model_meta']
