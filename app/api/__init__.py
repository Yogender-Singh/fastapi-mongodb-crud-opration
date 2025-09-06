from fastapi import APIRouter
from app.api.item import router as item_router

router = APIRouter()
router.include_router(item_router)
