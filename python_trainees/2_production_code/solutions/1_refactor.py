"""Module for generating a daily sales report.

The sales report includes these statistics:

  1. Number of unique customers.
  2. Total sales value.
  3. Total number of products sold.
  4. Average sales value per customer.
  5. Average number of products sold per customer.
  6. Highest valued customer.
  7. Highest valued product.
"""
import datetime as dt
from collections import Counter


# Report date should be provided as YYYY-MM-DD
REPORT_DATE = "2023-1-15"

# Absolute path or relative to the script location
SALES_PATH = "../../0_data/sales/transactions.csv"

REPORT_TEMPLATE = """
===============================================================
Report for:                           {report_date:>25s}
---------------------------------------------------------------
Aantal klanten:                       {total_customers:25.0f}
Totaal waarde:                        {total_sales:25.2f}
Totaal producten                      {total_products:25.0f}
---------------------------------------------------------------
Gemiddeld bedrag per klant:           {average_sales:25.2f}
Gemiddeld producten per klant:        {average_products:25.2f}
---------------------------------------------------------------
Beste klant:                          {best_customer:>25s}
Beste klant waarde:                   {best_customer_value:25.2f}
Beste product                         {best_product:>25s}
Beste product waard                   {best_product_value:25.2f}
===============================================================
"""


def read_sales_data(sales_path, report_date):
    """Read sales data from the prodived path.

    Parameters
    ----------
    sales_path : str
        Path to the sales data as string.
    report_date : str
        Report date as "YYYY-MMM-DD" string.

    Returns
    -------
    list
        List of sales records (dicts) for the provided date.
    """
    report_date = dt.datetime.strptime(report_date, "%Y-%m-%d")

    records = []
    with open(sales_path, "r", encoding="utf-8") as sales_file:
        header = next(sales_file).strip().split(",")

        for line in sales_file:
            # Create records with column names
            values = line.strip().split(",")
            record = {column: value for column, value in zip(header, values)}

            # Convert and check date
            record["transaction_date"] = dt.datetime.strptime(
                record["transaction_date"], "%Y-%m-%d"
            )
            if record["transaction_date"] != report_date:
                continue

            # Numeric records are read as strings
            for column in "quantity", "price", "total":
                record[column] = float(record[column])

            records.append(record)

    return records


def compute_totals(sales_data):
    """Compute total sales, number of products sold and number of customers.

    Parameters
    ----------
    sales_data
        List of sales data records (dicts).

    Returns
    -------
    float, float, int
        Tuple of total revenue, number of products sold, and
        number of customers.
    """
    total_sales = 0
    total_products = 0
    customers = []

    for record in sales_data:
        total_sales += record["total"]
        total_products += record["quantity"]
        if record["customer_id"] not in customers:
            customers.append(record["customer_id"])

    return total_sales, total_products, len(customers)


def compute_best(sales_data, group_column, value_column):
    """Compute best performer per group.

    Parameters
    ----------
    sales_data
        List of sales data records (dicts).
    group_column : str
        Column to aggregate the data by.
    value_column : str
        Columnt to aggragate values from.

    Returns
    -------
    str, float
        Best group and associated sales value.
    """
    counter = Counter()
    for record in sales_data:
        counter.update({record[group_column]: record[value_column]})

    return counter.most_common(1)[0]


def main():
    """Main program routine."""
    sales_data = read_sales_data(SALES_PATH, REPORT_DATE)

    total_sales, total_products, total_customers = compute_totals(sales_data)
    best_customer, best_customer_value = compute_best(
        sales_data, "customer_id", "total"
    )
    best_product, best_product_value = compute_best(
        sales_data, "product_id", "total"
    )

    print(
        REPORT_TEMPLATE.format(
            report_date=REPORT_DATE,
            total_sales=total_sales,
            total_products=total_products,
            total_customers=total_customers,
            average_sales=total_sales / total_customers,
            average_products=total_products / total_customers,
            best_customer=best_customer,
            best_customer_value=best_customer_value,
            best_product=best_product,
            best_product_value=best_product_value,
        )
    )


if __name__ == "__main__":
    main()
