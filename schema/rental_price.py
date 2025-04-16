from pydantic import BaseModel, Field, field_validator
from typing import List


class PickLocationCheckInput(BaseModel):
    pickup: List[str] = Field(description="Array of pickup locations")

    @field_validator("pickup")
    def validate_pickup(cls, value):
        print("inside PickLocationCheckInput", value)
        return value


class PickDropLocationCheckInput(PickLocationCheckInput):
    dropoff: List[str] = Field(description="Array of drop off locations")


class EstimateBusRentalPriceInput(PickDropLocationCheckInput):
    passengers: int = Field(description="Total number of passengers travelling")
