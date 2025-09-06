from motor.motor_asyncio import AsyncIOMotorCollection
from typing import Any, Dict


class MongoCRUD:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create(self, data: Dict[str, Any]) -> str:
        result = await self.collection.insert_one(data)
        return str(result.inserted_id)

    async def get(self, query: Dict[str, Any]) -> Dict[str, Any]:
        return await self.collection.find_one(query)

    async def update(self, query: Dict[str, Any], data: Dict[str, Any]) -> int:
        result = await self.collection.update_one(query, {"$set": data})
        return result.modified_count

    async def delete(self, query: Dict[str, Any]) -> int:
        result = await self.collection.delete_one(query)
        return result.deleted_count
