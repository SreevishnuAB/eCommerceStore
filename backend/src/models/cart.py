from typing import List
from pydantic import BaseModel, field_validator


class CartItem(BaseModel):
    itemId: str
    itemName: str
    quantity: int
    amount: float

    @field_validator('quantity', mode='after')
    @classmethod
    def ensure_non_zero_quantity(cls, quantity: int) -> int:  
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")
        return quantity
    
    @field_validator('amount', mode='after')
    @classmethod
    def ensure_non_zero_amount(cls, amount: float) -> float:
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        return amount

class Cart(BaseModel):
    cartItems: List[CartItem]