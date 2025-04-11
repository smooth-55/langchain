# Define the tools/functions
def estimate_bus_rental_price(pickup, dropoff, passengers):
    """Estimate the bus rental price based on locations and passenger count"""
    # This is a mock implementation - replace with your actual pricing logic
    print(pickup, dropoff, passengers, "estimate bus")
    return f"The estimated price is 200"

def pickup_location_check(pickup):
    """Check if pickup location is serviceable"""
    print("checking pickup location", pickup)
    # Mock implementation - replace with your actual location check
    return f"pickup_location_check:: Yes, we provide service from {pickup}"

def pick_drop_location_check(pickup, dropoff):
    """Check if the route between pickup and dropoff is serviceable"""
    print(pickup, "argsss", dropoff)
    # Mock implementation - replace with your actual route check
    return f"pick_drop_location_check:: Yes, we provide service from those"