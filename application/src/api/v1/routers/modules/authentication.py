import fastapi
import fastapi.security
import sqlalchemy.orm
import starlette.status

from src.core.log import log

from src.core.session.session import session

from src.core.schemas.user import CreateUser, UserAccount
from src.core.jwt.jwt import (
    create_access_token, verify_access_token,
    JWTBearer
)




router = fastapi.APIRouter()
authentication_schema = fastapi.security.HTTPBearer()





# Inicio de sesión.
@router.post(
    path='/sign-in',
    tags=['Autenticación'],
)
async def sign_in(UserAccount: UserAccount, request: fastapi.Request, session: sqlalchemy.orm.Session = fastapi.Depends(session)):
    return


# Creación de cuenta de usuario.
@router.post(
    path='/sign-up',
    status_code=starlette.status.HTTP_201_CREATED,
    tags=['Autenticación'],
)
async def sign_up(User: CreateUser, session: sqlalchemy.orm.Session = fastapi.Depends(session)):
    return



# Validador de sesión.
@router.post(
    path='/verify/session',
    tags=['Autenticación'],
    dependencies=[fastapi.Depends(JWTBearer())]
)
async def validate_session(Authorization: str, request: fastapi.Request, session: sqlalchemy.orm.Session = fastapi.Depends(session)):
    return


