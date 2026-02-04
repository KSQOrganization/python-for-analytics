"""Pytest configuration and fixtures for online-retail-analytics tests."""

import pytest


@pytest.fixture
def sample_data():
    """Provide sample ecommerce transaction data for testing."""
    return {
        "transactions": [
            {"transaction_id": "T001", "customer_id": "C001", "amount": 100.0},
            {"transaction_id": "T002", "customer_id": "C002", "amount": 200.0},
            {"transaction_id": "T003", "customer_id": "C001", "amount": 150.0},
        ]
    }


@pytest.fixture
def kedro_context():
    """Provide a Kedro context for integration tests."""
    # This will be implemented when pipelines are added
    pass
