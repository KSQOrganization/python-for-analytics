"""Unit test example for online-retail-analytics."""


def test_sample_data_structure(sample_data):
    """Test that sample data has the expected structure."""
    assert "transactions" in sample_data
    assert len(sample_data["transactions"]) == 3
    assert sample_data["transactions"][0]["transaction_id"] == "T001"


def test_sample_data_values(sample_data):
    """Test that sample data has valid values."""
    for transaction in sample_data["transactions"]:
        assert "transaction_id" in transaction
        assert "customer_id" in transaction
        assert "amount" in transaction
        assert transaction["amount"] > 0
