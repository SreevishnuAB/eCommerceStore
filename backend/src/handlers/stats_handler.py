from typing import List
from src.handlers.discount_handler import DiscountHandler
from src.models.cart import CartItem


class StatsHandler:
    def __init__(self, discount_handler: DiscountHandler):
        self._total_item_count = 0
        self._total_purchase_amount = 0.0
        self._discount_handler = discount_handler
        self._total_discount = 0.0
        self._order_count = 0

    @property
    def total_item_count(self) -> int:
        """
        Get the total number of items in the cart.
        """
        return self._total_item_count
    
    @total_item_count.setter
    def total_item_count(self, count: int) -> None:
        """
        Set the total number of items in the cart.
        """
        self._total_item_count = count

    @property
    def total_purchase_amount(self) -> float:
        """
        Get the total purchase amount.
        """
        return self._total_purchase_amount
    
    @total_purchase_amount.setter
    def total_purchase_amount(self, amount: float) -> None:
        """
        Set the total purchase amount.
        """
        self._total_purchase_amount = amount

    @property
    def total_discount(self) -> float:
        """
        Get the total discount amount.
        """
        self._total_discount = self._discount_handler.total_discount
        return self._total_discount
    
    @total_discount.setter
    def total_discount(self, discount: float) -> None:
        """
        Set the total discount amount.
        """
        self._discount_handler.total_discount = discount

    @property
    def order_count(self) -> int:
        """
        Get the total number of orders.
        """
        return self._order_count
    
    @order_count.setter
    def order_count(self, count: int) -> None:
        """
        Set the total number of orders.
        """
        self._order_count = count

    def is_order_eligible_for_discount(self) -> bool:
        """
        Check if the order is eligible for a discount.
        """

        # Every 3rd order is eligible for a discount, for demonstration purposes
        if self.order_count + 1 % 3 == 0:
            return True
        return False

    def update_total_item_count(self, cart_items: List[CartItem]) -> None:
        """
        Update the total number of items in the cart.
        """
        self.total_item_count += len(cart_items)

    def update_total_purchase_amount(self, amount_payable: float) -> None:
        """
        Update the total purchase amount.
        """
        self.total_purchase_amount += amount_payable

    def get_discount_codes(self) -> List[str]:
        """
        Get the list of discount codes.
        """
        return self._discount_handler.get_discount_codes()
