from decimal import Decimal

from pydantic import BaseModel, Field


class Schema(BaseModel):
    name: str = Field(max_length=60)
    current_price: Decimal = Field(ge=0, max_digits=11, decimal_places=4)
