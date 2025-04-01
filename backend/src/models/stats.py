from pydantic import BaseModel


class Stats(BaseModel):
    totalItemCount: int
    totalPurchaseAmount: float
    totalDiscount: float
    discountCodes: list[str]
    