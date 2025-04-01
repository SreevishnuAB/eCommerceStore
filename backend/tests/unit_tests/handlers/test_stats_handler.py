import pytest

from src.handlers.stats_handler import StatsHandler


def test_is_order_eligible_for_discount():
    stats_handler = StatsHandler()
    stats_handler.order_count = 5
    assert stats_handler.is_order_eligible_for_discount() is True


def test_is_order_eligible_for_discount_not_eligible():
    stats_handler = StatsHandler()
    stats_handler.order_count = 3
    assert stats_handler.is_order_eligible_for_discount() is False


def test_update_total_item_count():
    stats_handler = StatsHandler()
    stats_handler.update_total_item_count(5)
    assert stats_handler.total_item_count == 5


def test_update_total_purchase_amount():
    stats_handler = StatsHandler()
    stats_handler.update_total_purchase_amount(100.0)
    assert stats_handler.total_purchase_amount == 100.0


def test_update_order_count():
    stats_handler = StatsHandler()
    stats_handler.update_order_count()
    assert stats_handler.order_count == 1