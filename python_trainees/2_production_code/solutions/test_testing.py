"""Unit tests for testing module."""
import pytest
from testing import compute_totals


def test_valid_transactions():
    """Test compute_totals using valid and complete input."""
    sales = [
        {"klant_id": 1, "aantal": 2, "prijs_totaal": 5},
        {"klant_id": 2, "aantal": 1, "prijs_totaal": 2.50},
        {"klant_id": 3, "aantal": 4, "prijs_totaal": 11.8},
    ]
    total_value = 5 + 2.5 + 11.8
    total_products = 2 + 1 + 4
    total_customers = 3

    assert compute_totals(sales) == (total_value, total_products, total_customers)


def test_multiple_transactions():
    """Test compute_totals using valid and complete input."""
    sales = [
        {"klant_id": 1, "aantal": 2, "prijs_totaal": 5},
        {"klant_id": 1, "aantal": 1, "prijs_totaal": 2.50},
        {"klant_id": 1, "aantal": 4, "prijs_totaal": 11.8},
    ]
    total_value = 5 + 2.5 + 11.8
    total_products = 2 + 1 + 4
    total_customers = 1

    assert compute_totals(sales) == (total_value, total_products, total_customers)


def test_error_empty_transactions():
    """Test error on empty transactions list."""
    with pytest.raises(ValueError) as error:
        compute_totals([])

    assert error.match("empty list")
