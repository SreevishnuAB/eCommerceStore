import logging
from src.models.cart import Cart
from fastapi import APIRouter

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/cart")


@router.put("")
def update_cart(cart: Cart):
    logger.info(f"Updating cart with items: {cart.cartItems}")
    return {"message": "Cart updated successfully"}

@router.get("")
def get_cart():
    return {"message": "Cart retrieved successfully"}