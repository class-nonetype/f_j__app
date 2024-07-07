import logging
import platform
import os
import dotenv
dotenv.load_dotenv()


from pathlib import Path
from datetime import datetime
from pytz import timezone


APPLICATION_DIRECTORY = Path(__file__).parent.parent.parent
SRC_DIRECTORY = (APPLICATION_DIRECTORY / 'src')
CORE_DIRECTORY = (SRC_DIRECTORY / 'core')
LOG_DIRECTORY = (CORE_DIRECTORY / 'logs')
STATIC_DIRECTORY = (SRC_DIRECTORY / 'static')
TEMPLATES_DIRECTORY = (SRC_DIRECTORY / 'templates')






print(os.getenv('TZ'))
TZ = timezone(zone=os.getenv('TZ'))



def create_directory(*args):
    return [directory.mkdir() for directory in args if not directory.exists()]



ALL = ['*']
ALLOWED = True



API_TITLE = 'Entorno de desarrollo: PAMC API'
API_DESCRIPTION = 'PAMC API'
API_VERSION = 'v1'
API_HOST = '0.0.0.0'
API_PORT = 80
API_TIMEZONE = TZ
API_PREFIX = {
    'STATIC': '/api/{0}/static'.format(API_VERSION),
    'APPLICATION': '/api/{0}/application'.format(API_VERSION),
    'AUTHENTICATION': '/api/{0}/authentication'.format(API_VERSION)
}
API_STATIC_PATH = '/static/'
API_STATIC_NAME = 'static'
create_directory()


LOG_FILE_NAME = '.log'
LOG_FILE = (LOG_DIRECTORY / LOG_FILE_NAME)
LOG_MESSAGE_FORMAT = '%(asctime)-20s %(levelname)-10s %(module)s.%(funcName)s: %(message)s'
LOG_DATE_FORMAT = '%d/%m/%Y %I:%M:%S %p'
LOG_FORMATTER = logging.Formatter(fmt=LOG_MESSAGE_FORMAT, datefmt=LOG_DATE_FORMAT)
LOGGER_NAME = 'development.app'
