from typing import Optional
from src.models.cart import Cart
from pydantic import BaseModel


class CheckoutResponse(BaseModel):
    amountPayable: float