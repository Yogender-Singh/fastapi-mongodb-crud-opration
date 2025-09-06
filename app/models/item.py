from pydantic import BaseModel, Field
from typing import Optional


class Item(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, example="Sample Item")
    description: Optional[str] = Field(
        None, max_length=200, example="A description of the item."
    )
    price: float = Field(..., gt=0, example=19.99)
