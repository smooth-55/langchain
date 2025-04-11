from langchain.tools import StructuredTool
from schema.rental_price import EstimateBusRentalPriceInput, PickDropLocationCheckInput, PickLocationCheckInput
from tools.definations import estimate_bus_rental_price, pick_drop_location_check, pickup_location_check

# Create tool instances 
tools = [
    StructuredTool.from_function(
        name="EstimateBusRentalPrice",
        func=lambda pickup,dropoff,passengers: estimate_bus_rental_price(
            pickup, 
            dropoff, 
            passengers
        ),
        description="Useful for estimating the price of bus rental. Input should be a dictionary with 'pickup', 'dropoff', and 'passengers' keys.",
        return_direct=True,
        args_schema=EstimateBusRentalPriceInput,

    ),
    StructuredTool.from_function(
        name="PickupLocationCheck",
        func=lambda pickup: pickup_location_check(pickup),
        description="Useful for checking if a pickup location is serviceable. Input should be the pickup location as a string.",
        return_direct=True,
        args_schema=PickLocationCheckInput,
    ),
    StructuredTool.from_function(
        name="PickDropLocationCheck",
        func=lambda pickup,dropoff: pick_drop_location_check(pickup, dropoff),
        description="Useful for checking if a route between pickup and dropoff locations is serviceable. Input should be a dictionary with 'pickup' and 'dropoff' keys.",
        return_direct=True,
        args_schema=PickDropLocationCheckInput,
    )
]