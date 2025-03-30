from fastapi import APIRouter
from . import views

router = APIRouter()
router.include_router(views.router)