"""
Data processing pipeline for online retail analytics.

This module contains nodes for cleaning, transforming, and enriching
online retail/ecommerce transaction data.
"""

import pandas as pd


def clean_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Clean raw transaction data by removing duplicates and handling missing values.

    Args:
        transactions: Raw transaction data

    Returns:
        Cleaned transaction data
    """
    # Remove duplicates
    cleaned = transactions.drop_duplicates()

    # Remove rows with missing critical fields
    cleaned = cleaned.dropna(subset=["InvoiceNo", "StockCode", "Quantity"])

    # Remove cancelled transactions (negative quantities)
    cleaned = cleaned[cleaned["Quantity"] > 0]

    # Remove invalid prices
    cleaned = cleaned[cleaned["UnitPrice"] > 0]

    return cleaned


def add_derived_features(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Add derived features to transaction data.

    Args:
        transactions: Cleaned transaction data

    Returns:
        Transaction data with derived features
    """
    # Calculate total amount
    transactions["TotalAmount"] = transactions["Quantity"] * transactions["UnitPrice"]

    # Extract date components
    if "InvoiceDate" in transactions.columns:
        transactions["InvoiceDate"] = pd.to_datetime(transactions["InvoiceDate"])
        transactions["Year"] = transactions["InvoiceDate"].dt.year
        transactions["Month"] = transactions["InvoiceDate"].dt.month
        transactions["DayOfWeek"] = transactions["InvoiceDate"].dt.dayofweek
        transactions["Hour"] = transactions["InvoiceDate"].dt.hour

    return transactions


def aggregate_customer_metrics(transactions: pd.DataFrame) -> pd.DataFrame:
    """
    Aggregate customer-level metrics from transaction data.

    Args:
        transactions: Transaction data with derived features

    Returns:
        Customer-level metrics
    """
    customer_metrics = (
        transactions.groupby("CustomerID")
        .agg(
            {
                "InvoiceNo": "nunique",  # Number of orders
                "TotalAmount": ["sum", "mean", "std"],  # Spending metrics
                "Quantity": "sum",  # Total items purchased
                "StockCode": "nunique",  # Unique products
            }
        )
        .reset_index()
    )

    # Flatten column names
    customer_metrics.columns = [
        "CustomerID",
        "OrderCount",
        "TotalSpend",
        "AvgOrderValue",
        "StdOrderValue",
        "TotalItemsPurchased",
        "UniqueProducts",
    ]

    return customer_metrics
