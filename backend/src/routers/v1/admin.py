from typing import Dict
from src.models.stats import Stats
from src.routers.dependencies import stats_handler
from fastapi import APIRouter
from fastapi.exceptions import HTTPException


router = APIRouter(prefix="/admin")

@router.get("/stats")
def get_stats()-> Stats:

    return Stats(
        totalItemCount=stats_handler.total_item_count,
        totalPurchaseAmount=stats_handler.total_purchase_amount,
        totalDiscount=stats_handler.total_discount,
        discountCodes=stats_handler.get_discount_codes()
    )

@router.get("/discount")
def get_discount_code() -> Dict[str, str]:
    """
    Check if the order is eligible for a discount and return the discount code if eligible
    """
    if not stats_handler.is_order_eligible_for_discount():
        raise HTTPException(
            status_code=400,
            detail="Order is not eligible for a discount",
        )
    discount_code = stats_handler.get_discount_code()
    return {
        "discountCode": discount_code}
