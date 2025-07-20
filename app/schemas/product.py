from typing import List
from pydantic import BaseModel

class SizeQuantity(BaseModel):
    size: str
    quantity: int

class ProductCreate(BaseModel):
    name: str
    price: float
    sizes: List[SizeQuantity]

class ProductOut(ProductCreate):
    id: str
