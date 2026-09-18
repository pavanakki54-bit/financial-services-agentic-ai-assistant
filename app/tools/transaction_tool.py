import json
from pathlib import Path
from typing import Any


DATA_FILE = (
    Path(__file__).resolve().parents[2]
    / "data"
    / "transactions.json"
)


def get_transaction(transaction_id: str) -> dict[str, Any] | None:
    """
    Look up a synthetic transaction by transaction ID.
    """

    with DATA_FILE.open("r", encoding="utf-8") as file:
        transactions = json.load(file)

    for transaction in transactions:
        if transaction["transaction_id"] == transaction_id:
            return transaction

    return None
