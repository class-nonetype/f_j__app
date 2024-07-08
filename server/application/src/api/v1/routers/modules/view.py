
import fastapi
import fastapi.security
import fastapi.templating
import starlette.status
import sqlalchemy.orm

from src.core.utils import TEMPLATES_DIRECTORY
from src.core.log import log
from src.core.database.session import database


router = fastapi.APIRouter()
template = fastapi.templating.Jinja2Templates(directory=TEMPLATES_DIRECTORY)


@router.get(path='/', status_code=starlette.status.HTTP_200_OK)
async def root(request: fastapi.Request, session: sqlalchemy.orm.Session = fastapi.Depends(database)):
    if session.is_active:
        return template.TemplateResponse(
            name='application.html',
            context={
                'request': request
            }
        )


