from typing import Annotated
from src.models.checkout import CheckoutResponse
from src.routers.dependencies import discount_handler, cart_handler
from fastapi import APIRouter, Query
from fastapi.exceptions import HTTPException


router = APIRouter(prefix="/checkout")

@router.get("")
def checkout_cart(discount_code: Annotated[str | None, Query(alias="discount-code")] = None) -> CheckoutResponse:
    amount_payable = cart_handler.get_cart_amount()
    if discount_code:
        if not discount_handler.is_discount_code_valid(discount_code):
            raise HTTPException(
                status_code=400,
                detail="Invalid discount code",
            )
        
        discount_amount = discount_handler.get_discount_amount(amount_payable)
        amount_payable -= discount_amount
    return CheckoutResponse(amountPayable=amount_payable)
