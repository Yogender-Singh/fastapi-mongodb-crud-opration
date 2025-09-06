from fastapi import APIRouter, HTTPException
from app.models.item import Item
from app.db.base import AsyncMongoCRUD
from motor.motor_asyncio import AsyncIOMotorClient
import os

from pydantic import BaseModel
from typing import Optional

router = APIRouter(prefix="/items", tags=["items"])

MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")
client = AsyncIOMotorClient(MONGO_URL)
db = client["testdb"]
collection = db["items"]
crud = AsyncMongoCRUD(collection)


# Pydantic response model for output validation

from uuid import UUID


class ItemResponse(BaseModel):
    id: Optional[UUID]
    name: str
    description: Optional[str] = None
    price: float


# POST endpoint with output validation


# POST endpoint with output validation


@router.post("/", response_model=ItemResponse)
async def create_item(item: Item):
    # Ensure UUID is set for new item
    item_data = item.dict()
    if not item_data.get("id"):
        item_data["id"] = item.id
    await crud.create(item_data)
    return ItemResponse(**item_data)


# Example endpoint for payload and output validation


# Example endpoint for payload and output validation
@router.post("/validate", response_model=ItemResponse)
async def validate_item_payload(item: Item):
    """
    Accepts an Item payload, validates it, and returns the same data as output.
    """
    return ItemResponse(id=None, **item.dict())


@router.get("/{id}", response_model=ItemResponse)
async def get_item(id: UUID):
    item = await crud.get({"id": str(id)})
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(**item)


@router.put("/{id}", response_model=ItemResponse)
async def update_item(id: UUID, item: Item):
    updated = await crud.update({"id": str(id)}, item.dict())
    if not updated:
        raise HTTPException(status_code=404, detail="Item not found")
    return ItemResponse(id=id, **item.dict())


@router.delete("/{id}")
async def delete_item(id: UUID):
    deleted = await crud.delete({"id": str(id)})
    if not deleted:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"deleted": deleted}
