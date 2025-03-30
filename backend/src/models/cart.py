from typing import List
from pydantic import BaseModel


class CartItem(BaseModel):
    itemId: int
    itemName: str
    quantity: int
    price: float


class Cart(BaseModel):
    cartItems: List[CartItem]