def transform_card(row):
    return {
        "event_version": "v1",
        "payment_id": row["card_txn_id"],
        "payment_type": "CARD",
        "customer_id": row["customer_ref"],
        "amount": float(row["txn_amount"]),
        "currency": row["txn_currency"],
        "status": row["txn_status"],
        "payment_method": row["card_type"],
        "merchant_name": row["merchant"],
        "counterparty": None,
        "event_timestamp": row["txn_time"],
        "source_system": "cards"
    }


def transform_transfer(row):
    return {
        "event_version": "v1",
        "payment_id": row["transfer_id"],
        "payment_type": "TRANSFER",
        "customer_id": row["user_id"],
        "amount": float(row["amount"]),
        "currency": row["currency"],
        "status": row["status"],
        "payment_method": "BANK_TRANSFER",
        "merchant_name": None,
        "counterparty": row["beneficiary"],
        "event_timestamp": row["transfer_time"],
        "source_system": "transfers"
    }


def transform_bill(row):
    return {
        "event_version": "v1",
        "payment_id": row["bill_id"],
        "payment_type": "BILL_PAYMENT",
        "customer_id": row["customer_id"],
        "amount": float(row["bill_amount"]),
        "currency": row["bill_currency"],
        "status": row["payment_status"],
        "payment_method": "ACCOUNT_BALANCE",
        "merchant_name": row["biller"],
        "counterparty": None,
        "event_timestamp": row["payment_time"],
        "source_system": "bill_payments"
    }
