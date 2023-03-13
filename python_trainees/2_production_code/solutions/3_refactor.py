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
import sys
import logging
import datetime as dt
from collections import Counter


# Report date should be provided as YYYY-MM-DD
REPORT_DATE = "2023-1-15"

# Absolute path or relative to the script location
SALES_PATH = "invalid/file/path"
REPORT_PATH = f"{REPORT_DATE}-report.txt"

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

# Create a logger and configure logging
logger = logging.getLogger("SalesReporter")
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)-8s - %(name)s - %(message)s",
    datefmt="%d-%m-%Y %H:%M:S",
)


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
    logger.info("Reading sales data for: %s.", report_date)
    logger.debug("Reading sales data from: '%s'.", sales_path)
    report_date = dt.datetime.strptime(report_date, "%Y-%m-%d")

    records = []

    # Error for file not found
    try:
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
                if record["datum"] != report_date:
                    continue

                # Numeric records are read as strings
                for column in "quantity", "price", "total":
                    record[column] = float(record[column])

                records.append(record)

    except FileNotFoundError:
        logger.error("Cannot find sales data file: '%s'.", sales_path)
        sys.exit(1)

    logger.debug("Read %d sales transactions.", len(records))
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
        Tuple of total sales, number of products sold, and
        number of customers.
    """
    logger.info("Computing sales totals on %d transactions.", len(sales_data))
    total_sales = 0
    total_products = 0
    customers = []

    for record in sales_data:

        # Error for missing data
        total_sales += record["total"]
        total_products += record["quantity"]
        if record["customer_id"] not in customers:
            customers.append(record["customer_id"])

    logger.debug("Total sales: %.2f.", total_sales)
    logger.debug("Total products: %.0f.", total_products)
    logger.debug("Total customers: %.0f.", len(customers))
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
    logger.info("Computing best '%s' based on '%s'.", group_column, value_column)
    counter = Counter()
    for record in sales_data:
        counter.update({record[group_column]: record[value_column]})

    best = counter.most_common(1)[0]
    logger.debug("Best %s: %s.", group_column, best[0])
    logger.debug("Best %s: %f.", value_column, best[1])
    return best


def write_report(report_path, report):
    """Write report to provided path.

    Parameters
    ----------
    report_path : str
        Path to write report to.
    report : str
        String containing the formatted report.
    """
    logger.info("Writing report to: '%s'.", report_path)
    with open(report_path, "w", encoding="utf-8") as report_file:
        report_file.write(report)


def main():
    """Main program routine."""
    logger.info("Generating sales report for %s.", REPORT_DATE)
    sales_data = read_sales_data(SALES_PATH, REPORT_DATE)

    total_sales, total_products, total_customers = compute_totals(sales_data)
    best_customer, best_customer_value = compute_best(
        sales_data, "customer_id", "total"
    )
    best_product, best_product_value = compute_best(
        sales_data, "product_id", "total"
    )

    report = REPORT_TEMPLATE.format(
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

    write_report(REPORT_PATH, report)


if __name__ == "__main__":
    main()
