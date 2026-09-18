from app.tools.transaction_tool import get_transaction


def test_existing_transaction():
    transaction = get_transaction("TXN-1002")

    assert transaction is not None
    assert transaction["transaction_id"] == "TXN-1002"
    assert transaction["merchant"] == "Northstar Electronics"
    assert transaction["amount"] == 249.99


def test_missing_transaction():
    transaction = get_transaction("TXN-9999")

    assert transaction is None
