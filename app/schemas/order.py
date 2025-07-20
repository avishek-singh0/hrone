
from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    user_id: str
    products: List[str]

class ProductBrief(BaseModel):
    id: str
    name: str
    size: str
    price: float

class OrderOut(BaseModel):
    order_id: str
    user_id: str
    products: List[ProductBrief]
