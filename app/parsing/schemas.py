from decimal import Decimal

from pydantic import BaseModel
from pydantic import Field


class Schema(BaseModel):
    name: str = Field(max_length=60, min_length=1)
    current_price: Decimal = Field(ge=0, max_digits=14, decimal_places=2)
