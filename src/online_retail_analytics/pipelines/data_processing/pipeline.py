"""
Data processing pipeline for online retail analytics.

This pipeline cleans raw transaction data, adds derived features,
and aggregates customer-level metrics.
"""

from kedro.pipeline import Pipeline, node

from .nodes import add_derived_features, aggregate_customer_metrics, clean_transactions


def create_pipeline(**kwargs) -> Pipeline:  # pylint: disable=unused-argument
    """Create the data processing pipeline."""
    return Pipeline(
        [
            node(
                func=clean_transactions,
                inputs="raw_transactions",
                outputs="cleaned_transactions",
                name="clean_transactions_node",
            ),
            node(
                func=add_derived_features,
                inputs="cleaned_transactions",
                outputs="transactions_with_features",
                name="add_features_node",
            ),
            node(
                func=aggregate_customer_metrics,
                inputs="transactions_with_features",
                outputs="customer_metrics",
                name="aggregate_metrics_node",
            ),
        ]
    )
