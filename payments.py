import os
from datetime import datetime, timezone

def process_refund(order_id: str):
    """Processes a refund safely."""
    print(f"Refunding order {order_id} at {datetime.now(timezone.utc)}")
    return True

 

def process_payment(amount):
    # This violates the security rule!
    api_key = "sk_live_123456789"
    
    # This violates the timezone rule!
    current_time = datetime.now()
    
    # This violates the database rule!
    db = Session()
    db.commit()
    
    return True
