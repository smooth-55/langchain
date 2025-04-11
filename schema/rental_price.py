from pydantic import BaseModel, Field
from typing import List

class PickLocationCheckInput(BaseModel):
    pickup: List[str] = Field(description="Array of pickup locations")

class PickDropLocationCheckInput(PickLocationCheckInput):
    dropoff: List[str] = Field(description="Array of drop off locations")

class EstimateBusRentalPriceInput(PickDropLocationCheckInput):
    passengers: int = Field(description="Total number of passengers travelling")