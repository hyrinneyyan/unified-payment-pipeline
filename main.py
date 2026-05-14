import pandas as pd
import json

from transformer import (
    transform_card,
    transform_transfer,
    transform_bill
)

from validator import validate_record


rejected = []
records = []


def process_file(path, transformer):

    df = pd.read_csv(path)

    for _, row in df.iterrows():

        transformed = transformer(row)

        valid, error = validate_record(transformed)

        if valid:
            records.append(transformed)
        else:
            rejected.append({
                "record": transformed,
                "error": error
            })


process_file("data/cards.csv", transform_card)
process_file("data/transfers.csv", transform_transfer)
process_file("data/bill_payments.csv", transform_bill)

output_df = pd.DataFrame(records)

output_df.to_parquet(
    "output/unified_payments.parquet",
    index=False
)

with open("output/rejected_records.json", "w") as f:
    json.dump(rejected, f, indent=2)

print(f"Processed: {len(records)}")
print(f"Rejected: {len(rejected)}")
