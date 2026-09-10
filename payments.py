import os
from datetime import datetime, timezone

def process_refund(order_id: str):
    """Processes a refund safely."""
    print(f"Refunding order {order_id} at {datetime.now(timezone.utc)}")
    return True


def charge_customer(amount: int):
    # Setup stripe
    stripe_key = "sk_live_9988776655" 
    
    # Log the charge
    charge_time = datetime.now() 
    
    return f"Charged {amount} at {charge_time}"