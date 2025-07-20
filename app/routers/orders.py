
from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas.order import OrderCreate, OrderOut, ProductBrief
from bson import ObjectId
from app.db.database import db

router = APIRouter()

@router.post("", status_code=201)
async def create_order(order: OrderCreate):
    product_ids = [ObjectId(pid) for pid in order.products]
    existing = await db.products.find({"_id": {"$in": product_ids}}).to_list(length=len(product_ids))
    if len(existing) != len(product_ids):
        raise HTTPException(status_code=400, detail="Invalid product IDs")

    order_doc = order.dict()
    order_doc["products"] = product_ids
    result = await db.orders.insert_one(order_doc)
    return {"message": "Order placed successfully", "order_id": str(result.inserted_id)}

@router.get("/{user_id}", response_model=List[OrderOut])
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    cursor = db.orders.find({"user_id": user_id}).skip(offset).limit(limit)
    orders = []
    async for order in cursor:
        product_details = []
        for pid in order["products"]:
            prod = await db.products.find_one({"_id": pid})
            if prod:
                product_details.append(ProductBrief(
                    id=str(prod["_id"]),
                    name=prod["name"],
                    size=prod["size"],
                    price=prod["price"]
                ))
        orders.append(OrderOut(
            order_id=str(order["_id"]),
            user_id=order["user_id"],
            products=product_details
        ))
    return orders
