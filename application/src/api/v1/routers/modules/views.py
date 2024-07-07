
import fastapi
import fastapi.security
import fastapi.templating
import starlette.status
import os
import pandas as pd

from src.core.utils import Directory
from src.core.log import log




router = fastapi.APIRouter()
template = fastapi.templating.Jinja2Templates(directory=Directory().templates)


@router.get(path='/', status_code=starlette.status.HTTP_200_OK)
async def root(request: fastapi.Request):
    return template.TemplateResponse(
        name='application.html',
        context={
            'request': request
        }
    )