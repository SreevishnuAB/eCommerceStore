from typing import List
from pydantic import BaseModel, field_validator


class CartItem(BaseModel):
    itemId: str
    itemName: str
    quantity: int
    price: float

    @field_validator('quantity', mode='after')
    @classmethod
    def ensure_non_zero_quantity(cls, quantity: int) -> int:  
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return quantity
    
    @field_validator('price', mode='after')
    @classmethod
    def ensure_non_zero_price(cls, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount

class Cart(BaseModel):
    cartItems: List[CartItem]