def migrate_v1_to_v2(record):

    record["event_version"] = "v2"

    record["country_code"] = "AE"
    record["processing_fee"] = round(
        record["amount"] * 0.015,
        2
    )

    return record
