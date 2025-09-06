from fastapi import APIRouter, HTTPException
from app.models.item import Item
from app.db.base import MongoCRUD
from motor.motor_asyncio import AsyncIOMotorClient
import os

from pydantic import BaseModel
from typing import Optional

router = APIRouter()

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["testdb"]
collection = db["items"]
crud = MongoCRUD(collection)


# Pydantic response model for output validation
class ItemResponse(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str] = None
    price: float


# POST endpoint with output validation
@router.post("/items", response_model=ItemResponse)
async def create_item(item: Item):
    item_id = await crud.create(item.dict())
    return ItemResponse(id=item_id, **item.dict())


# Example endpoint for payload and output validation
@router.post("/items/validate", response_model=ItemResponse)
async def validate_item_payload(item: Item):
    """
    Accepts an Item payload, validates it, and returns the same data as output.
    """
    return ItemResponse(id=None, **item.dict())


@router.get("/items/{name}")
async def get_item(name: str):
    item = await crud.get({"name": name})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.put("/items/{name}")
async def update_item(name: str, item: Item):
    updated = await crud.update({"name": name}, item.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"updated": updated}


@router.delete("/items/{name}")
async def delete_item(name: str):
    deleted = await crud.delete({"name": name})
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": deleted}
