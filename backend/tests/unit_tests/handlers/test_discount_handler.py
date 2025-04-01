from src.handlers.discount_handler import DiscountHandler


def test_is_discount_code_valid_unknown_discount_code():
    discount_handler = DiscountHandler()
    assert not discount_handler.is_discount_code_valid("123")


def test_is_discount_code_valid_previously_used_code():
    discount_handler = DiscountHandler()
    discount_handler.discount_codes["123"] = True
    assert not discount_handler.is_discount_code_valid("123")


def test_is_discount_code_valid_valid_code():
    discount_handler = DiscountHandler()
    discount_handler.discount_codes["123"] = False
    assert discount_handler.is_discount_code_valid("123")
    assert discount_handler.discount_codes["123"]


def test_create_discount_code():
    discount_handler = DiscountHandler()
    discount_code = discount_handler.create_discout_code()
    assert len(discount_code) == 10
    
def test_get_discount_amount():
    discount_handler = DiscountHandler()
    total_amount = 100.0
    discount = discount_handler.get_discount_amount(total_amount)
    assert discount == 10.0

    # check if the discount amounts are compounded
    discount_handler.get_discount_amount(total_amount)
    assert discount_handler.total_discount == 20.0


def test_get_discount_codes():
    discount_handler = DiscountHandler()
    discount_handler.discount_codes["123"] = False
    discount_handler.discount_codes["456"] = False
    discount_codes = discount_handler.get_discount_codes()
    assert len(discount_codes) == 2
    assert "123" in discount_codes
    assert "456" in discount_codes