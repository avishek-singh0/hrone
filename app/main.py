
from fastapi import FastAPI
from app.routers import products, orders
from app.db.database import connect_to_mongo
import uvicorn

app = FastAPI()

@app.on_event("startup")
async def startup_db():
    await connect_to_mongo()

app.include_router(products.router, prefix="/products", tags=["Products"])
app.include_router(orders.router, prefix="/orders", tags=["Orders"])

@app.get("/")
def root():
    return {"message": "HROne Backend Intern API"}

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
