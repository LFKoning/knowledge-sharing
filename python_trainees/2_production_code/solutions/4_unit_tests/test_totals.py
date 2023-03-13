"""Unit tests for testing module."""
import pytest
from totals import compute_totals


def test_valid_transactions():
    """Test compute_totals using valid and complete input."""
    sales = [
        {"customer_id": 1, "quantity": 2, "total": 5},
        {"customer_id": 2, "quantity": 1, "total": 2.50},
        {"customer_id": 3, "quantity": 4, "total": 11.8},
    ]
    total_sales = 5 + 2.5 + 11.8
    total_products = 2 + 1 + 4
    total_customers = 3

    assert compute_totals(sales) == (total_sales, total_products, total_customers)


def test_multiple_transactions():
    """Test compute_totals using valid and complete input."""
    sales = [
        {"customer_id": 1, "quantity": 2, "total": 5},
        {"customer_id": 1, "quantity": 1, "total": 2.50},
        {"customer_id": 1, "quantity": 4, "total": 11.8},
    ]
    total_sales = 5 + 2.5 + 11.8
    total_products = 2 + 1 + 4
    total_customers = 1

    assert compute_totals(sales) == (total_sales, total_products, total_customers)


def test_error_empty_transactions():
    """Test error on empty transactions list."""
    with pytest.raises(ValueError) as error:
        compute_totals([])

    assert error.match("empty list")
