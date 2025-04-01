import logging

from fastapi import APIRouter

from src.routers.dependencies import cart_handler
from src.models.cart import Cart
logger = logging.getLogger(__name__)


router = APIRouter(prefix="/cart")


@router.put("")
def update_cart(cart: Cart):
    logger.info(f"Updating cart with items: {cart.cartItems}")
    cart_handler.cart = cart.cartItems
    return {"message": "Cart updated successfully"}


@router.get("")
def get_cart() -> Cart:
    return Cart(cartItems=cart_handler.cart if cart_handler.cart else [])


@router.delete("")
def reset_cart():
    cart_handler.cart = []
    return {"message": "Cart reset successfully"}