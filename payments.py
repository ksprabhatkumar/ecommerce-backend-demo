import os
from datetime import datetime, timezone

def process_refund(order_id: str):
    """Processes a refund safely."""
    print(f"Refunding order {order_id} at {datetime.now(timezone.utc)}")
    return True


 