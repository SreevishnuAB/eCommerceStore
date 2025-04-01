"""
Dependencies for the E-Commerce Store API.

Instantiated objects for handlers to maintain data for a single boot of the application.
"""

from src.handlers.stats_handler import StatsHandler
from src.handlers.cart_handler import CartHandler
from src.handlers.discount_handler import DiscountHandler


cart_handler = CartHandler()
discount_handler = DiscountHandler()
stats_handler = StatsHandler(discount_handler=discount_handler)