from src.routers.v1 import admin
from fastapi import FastAPI

from src.routers.v1.cart import router as cart_router
from src.routers.v1.checkout import router as checkout_router
from src.routers.v1.admin import router as admin_router


ROUTE_PREFIX = "/e-com-store/v1"

app = FastAPI(title="E-Commerce Store")

app.include_router(cart_router, prefix=ROUTE_PREFIX, tags=["cart"])
app.include_router(checkout_router, prefix=ROUTE_PREFIX, tags=["checkout"])
app.include_router(admin_router, prefix=ROUTE_PREFIX, tags=["admin"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)