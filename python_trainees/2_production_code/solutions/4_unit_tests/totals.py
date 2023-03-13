"""Module with functions for unit testing."""


def compute_totals(sales_data):
    """Compute total sales, number of products sold and number of customers.

    Parameters
    ----------
    sales_data
        List of sales data records (dicts).

    Returns
    -------
    float, float, int
        Tuple of total sales, number of products sold, and
        number of customers.

    Raises
    ------
    ValueError
        When sales_data is not a list or an empty list.
    """
    if not sales_data or not isinstance(sales_data, list):
        raise ValueError("Sales data is not a list or an empty list.")

    total_sales = 0
    total_products = 0
    customers = []

    for record in sales_data:
        total_sales += record["total"]
        total_products += record["quantity"]
        if record["customer_id"] not in customers:
            customers.append(record["customer_id"])

    return total_sales, total_products, len(customers)
