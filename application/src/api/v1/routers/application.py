import fastapi
import fastapi.security
import fastapi.templating

from src.core.log import log
from src.api.v1.routers.modules.views import router as view



router = fastapi.APIRouter()
router.include_router(router=view)
