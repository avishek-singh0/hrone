
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    size: str
    price: float

class ProductOut(ProductCreate):
    id: str
