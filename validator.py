from pydantic import BaseModel, ValidationError
from typing import Optional


class PaymentEvent(BaseModel):
    event_version: str
    payment_id: str
    payment_type: str
    customer_id: str
    amount: float
    currency: str
    status: str
    payment_method: str
    merchant_name: Optional[str]
    counterparty: Optional[str]
    event_timestamp: str
    source_system: str


def validate_record(record):
    try:
        PaymentEvent(**record)
        return True, None
    except ValidationError as e:
        return False, str(e)
