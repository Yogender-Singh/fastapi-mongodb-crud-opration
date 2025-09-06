from pydantic import BaseModel, Field
from typing import Optional


from uuid import uuid4, UUID


class Item(BaseModel):
    id: Optional[UUID] = Field(
        default_factory=uuid4, example="123e4567-e89b-12d3-a456-426614174000"
    )
    name: str = Field(..., min_length=3, max_length=50, example="Sample Item")
    description: Optional[str] = Field(
        None, max_length=200, example="A description of the item."
    )
    price: float = Field(..., gt=0, example=19.99)
