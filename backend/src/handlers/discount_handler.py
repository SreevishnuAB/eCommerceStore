import dis
import secrets


class DiscountHandler:

    def __init__(self):
        self.discount_codes = {}
        self.total_discount = 0

    def validate_discount_code(self, discount_code: str) -> bool:
        """
        Validate the discount code.
        """
        if discount_code in self.discount_codes and not self.discount_codes[discount_code]:
            # set value for the discount code to True to denote that is used
            self.discount_codes[discount_code] = True
            return True
        return False
    
    def create_discout_code(self) -> None:
        """
        Create a new discount code.
        """

        # creates a random unique string of length 10
        discount_code = secrets.token_hex(10)
        self.discount_codes[discount_code] = False
        return discount_code


