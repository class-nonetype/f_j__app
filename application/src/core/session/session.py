
import sqlalchemy.orm
from src.core.log import log
from src.core.database.session import session as Session

async def session():
    database: sqlalchemy.orm.Session = Session()

    try:
        yield database

    except Exception as exception:
        log.exception(exception)

    finally:
        database.close()