
from fastapi import APIRouter
from typing import List, Optional
from app.schemas.product import ProductCreate, ProductOut
from app.db.database import db
from bson import ObjectId

router = APIRouter()

@router.post("", status_code=201)
async def create_product(product: ProductCreate):
    product_dict = product.dict()
    result = await db.products.insert_one(product_dict)
    return {"message": "Product created successfully", "id": str(result.inserted_id)}

@router.get("", response_model=List[ProductOut])
async def list_products(name: Optional[str] = None, size: Optional[str] = None,
                        limit: int = 10, offset: int = 0):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if size:
        query["size"] = size

    cursor = db.products.find(query).skip(offset).limit(limit)
    products = []
    async for doc in cursor:
        doc["id"] = str(doc["_id"])
        products.append(ProductOut(**doc))
    return products
