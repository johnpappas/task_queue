import os
import property_utils
"""
    The env variables are stored in environment specific files
        name per the following:  build_env_props_[environment].sh
        where environment is either dev, staging or production.

    When this file is executed, it needs to be done sourced like below:
        <prompt>$source /path/to/file/build_env_props_staging.sh

    The file needs to be executable before it is sourced:
        i.e., chmod +x build_env_props_staging.sh

    NOTE:  the file APP_NAME must contain a value specific to this project
    so that each project can have unique environment variables:
    Example: REDIS_HOST is exported by the env_props shell script
    to TASK_QUEUE_REDIS_HOST.
    This module looks for the value TASK_QUEUE_REDIS_HOST
    and makes it available to the rest of the application by its
    generic name 'REDIS_HOST'

"""



# logging file path
LOGGING_CONF_FILE_PATH = os.environ['PWD']+'/logging.conf'
# Redis general properties
REDIS_HOST = os.environ[property_utils.get_app_name_prefix() + 'REDIS_HOST']
REDIS_PORT = os.environ[property_utils.get_app_name_prefix() + 'REDIS_PORT']
REDIS_DB = os.environ[property_utils.get_app_name_prefix() + 'REDIS_DB']
REDIS_PASSWORD = os.environ[property_utils.get_app_name_prefix() + 'REDIS_PASS']
# Redis queue properties
REDIS_QUEUE_LISTING_URL_NAMESPACE = os.environ[property_utils.get_app_name_prefix() + 'REDIS_QUEUE_LISTING_URL_NAMESPACE']
# Redis cache properties
REDIS_CACHE_LISTING_UUID_NAMESPACE = os.environ[property_utils.get_app_name_prefix() + 'REDIS_CACHE_LISTING_UUID_NAMESPACE']
REDIS_CACHE_KEY_EXPIRY = os.environ[property_utils.get_app_name_prefix() + 'REDIS_CACHE_KEY_EXPIRY']
# Database properties
RDS_DB_NAME = os.environ[property_utils.get_app_name_prefix() + 'RDS_DB_NAME']
RDS_DB_USERNAME = os.environ[property_utils.get_app_name_prefix() + 'RDS_DB_USERNAME']
RDS_DB_PASS = os.environ[property_utils.get_app_name_prefix() + 'RDS_DB_PASS']
RDS_DB_HOSTNAME = os.environ[property_utils.get_app_name_prefix() + 'RDS_DB_HOSTNAME']
RDS_DB_PORT = os.environ[property_utils.get_app_name_prefix() + 'RDS_DB_PORT']
# SUPERPROXY properties
SUPERPROXY_USERNAME = os.environ[property_utils.get_app_name_prefix() + 'SUPERPROXY_USERNAME']
SUPERPROXY_PASS = os.environ[property_utils.get_app_name_prefix() + 'SUPERPROXY_PASS']
SUPERPROXY_PORT = os.environ[property_utils.get_app_name_prefix() + 'SUPERPROXY_PORT']

