from typing import List
from src.models.cart import CartItem


class CartHandler:
    def __init__(self):
        
        self._cart: List[CartItem] = None

    @property
    def cart(self) -> List[CartItem]:
        return self._cart
    
    @cart.setter
    def cart(self, cart: List[CartItem]) -> None:
        self._cart = cart

    def get_cart_amount(self) -> float:
        """
        Calculate the total cart value.
        """
        amount = 0
        for item in self.cart:
            amount += item['quantity'] * item['price']
        return amount
    
    def get_cart_count(self) -> int:
        """
        Calculate the total number of items in the cart.
        """
        count = 0
        for item in self.cart:
            count += item['quantity']
        return count
    
    def get_cart(self) -> List[CartItem]:
        """
        Get cart items.
        """
        return self.cart

    
