from src.models.cart import Cart, CartItem
import pytest
from src.handlers.cart_handler import CartHandler

def test_get_empty_cart():
    cart_handler = CartHandler()
    
    with pytest.raises(ValueError):
        cart_handler.get_cart_amount()


def test_get_cart_amount_empty_cart():
    cart_handler = CartHandler()
    
    with pytest.raises(ValueError):
        cart_handler.get_cart_amount()


def test_get_cart():
    cart_handler = CartHandler()
    cart_handler.cart = [CartItem(itemId="123", itemName="Test Item", quantity=2, price=10.0)]
    assert cart_handler.get_cart()


def test_get_cart_count():
    cart_handler = CartHandler()
    cart_handler.cart = [CartItem(itemId="123", itemName="Test Item", quantity=2, price=10.0)]
    assert cart_handler.get_cart_count() == 1


def test_get_cart_count():
    cart_handler = CartHandler()
    cart_handler.cart = [CartItem(itemId="123", itemName="Test Item", quantity=2, price=10.0)]
    assert cart_handler.get_cart_amount() == 20.0