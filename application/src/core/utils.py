import logging
import os
import dotenv
dotenv.load_dotenv()


from pathlib import Path
from datetime import datetime
from pytz import timezone


ALL = ['*']
ALLOWED = True

TZ = timezone(zone=os.getenv('TZ'))
TIME_ALLOWED_MODIFICATION = os.getenv('TIME_ALLOWED_MODIFICATION', None)
SECRET_KEY = os.getenv('SECRET_KEY', None)
DATABASE_URL = os.getenv('DATABASE_URL', None)
print(DATABASE_URL)

API_TITLE = 'Entorno de desarrollo: PAMC API'
API_DESCRIPTION = 'PAMC API'
API_VERSION = 'v1'
API_HOST = '0.0.0.0'
API_PORT = 80
API_TIMEZONE = TZ
API_PREFIX = {
    'STATIC': '/api/{0}/static'.format(API_VERSION),
    'APPLICATION': '/api/{0}/application'.format(API_VERSION),
    'APPLICATION': '',
    'AUTHENTICATION': '/api/{0}/authentication'.format(API_VERSION)
}
API_STATIC_PATH = '/static'
API_STATIC_NAME = 'static'



APPLICATION_DIRECTORY = Path(__file__).parent.parent.parent

SRC_DIRECTORY = (APPLICATION_DIRECTORY / 'src')
CORE_DIRECTORY = (SRC_DIRECTORY / 'core')
LOG_DIRECTORY = (CORE_DIRECTORY / 'logs')
LOG_FILE_NAME = '.log'
LOG_FILE = (LOG_DIRECTORY / LOG_FILE_NAME)
LOG_MESSAGE_FORMAT = '%(asctime)-20s %(levelname)-10s %(module)s.%(funcName)s: %(message)s'
LOG_DATE_FORMAT = '%d/%m/%Y %I:%M:%S %p'
LOG_FORMATTER = logging.Formatter(fmt=LOG_MESSAGE_FORMAT, datefmt=LOG_DATE_FORMAT)
LOGGER_NAME = 'development.app'

STATIC_DIRECTORY = (SRC_DIRECTORY / 'static')
TEMPLATES_DIRECTORY = (SRC_DIRECTORY / 'templates')

ALLOWED_FILE_EXTENSIONS = (
    '.pdf', '.xls', '.xlsx', '.xlsm',
    '.doc', '.docx', '.csv', '.txt', 
    '.ppt', '.pptx', '.msg', '.png',
    '.jpg', '.jpeg', '.zip', '.rar',
    '.7z',
)

def create_directory(*args):
    return [directory.mkdir() for directory in args if not directory.exists()]



# Obtención de la fecha en base a la zona horaria local.
def get_datetime() -> datetime:
    return datetime.now(tz=TZ)

def get_modification_date_status(date: datetime | str) -> bool:
    current_date = get_datetime()
    
    # Si el día de la semana es Miércoles o Jueves, al tiempo habilitado de modificación
    # se le sumarán 48 horas hábiles.
    if current_date.weekday() == 3 or current_date.weekday() == 4:

        # Redondeo de hora para que sea lo más exacto posible
        current_date.replace(microsecond=0)
        time_allowed_modification = int(TIME_ALLOWED_MODIFICATION) + 48

    else:
        current_date.replace(microsecond=0)
        time_allowed_modification = int(TIME_ALLOWED_MODIFICATION)
    
    creation_date = date
    creation_date = TZ.localize(creation_date)
    
    # Fecha de finalización de modificación
    modification_deadline = creation_date + datetime.timedelta(hours=time_allowed_modification)
    
    if current_date > modification_deadline:
        return False
    else:
        return True

create_directory(LOG_DIRECTORY)

