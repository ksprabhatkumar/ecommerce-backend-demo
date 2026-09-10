import os
from datetime import datetime, timezone

def process_refund(order_id: str):
    """Processes a refund safely."""
    print(f"Refunding order {order_id} at {datetime.now(timezone.utc)}")
    return True


def process_secret_payment():
    # Blatant violation 1: Hardcoded secret
    stripe_token = "sk_live_super_secret_password_12345"
    
    # Blatant violation 2: Local timezone
    transaction_time = datetime.now()
    
    # Blatant violation 3: Direct DB session
    db = Session()
    db.commit()
    
    return True