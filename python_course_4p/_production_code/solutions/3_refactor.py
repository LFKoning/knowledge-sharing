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


# Report date should be provided as YYYY-MM-DD.
REPORT_DATE = "2023-01-15"

# Absolute path or relative to the script location.
SALES_PATH = "invalid/file/path"

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
Beste product:                        {best_product:>25s}
Beste product waarde:                 {best_product_value:25.2f}
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

    records = []

    # Error for file not found
    try:
        with open(sales_path, "r", encoding="utf-8") as sales_file:
            header = next(sales_file).strip().split(",")

            for line in sales_file:
                # Create records with column names.
                values = line.strip().split(",")
                record = {column: value for column, value in zip(header, values)}

                # Filter by reporting date.
                if record["transaction_date"] != report_date:
                    continue

            # Numeric records are read as strings.
            for column in "quantity", "line_nr", "price", "total":
                record[column] = float(record[column])

                records.append(record)

    except FileNotFoundError:
        logger.error("Cannot find sales data file: '%s'.", sales_path)
        sys.exit(1)

    logger.debug("Read %d sales transactions.", len(records))
    return records


def count_unique(sales_data, column_name):
    """Compute unique items in a column.

    Parameters
    ----------
    sales_data : list
        List of sales data records (dicts).
    column_name : str
        Name of the column to process.

    Returns
    -------
    int
        Number of unique values.
    """
    logger.info("Computing unique values for column: %s", column_name)

    if column_name not in sales_data[0]:
        msg = f"Column {column_name} not present in sales data."
        logger.error(msg)
        raise RuntimeError(msg)

    unique = {record[column_name] for record in sales_data}

    logger.debug("Number of unique values: %d", len(unique))
    return len(unique)


def compute_total(sales_data, column_name):
    """Compute total value for a column.

    Parameters
    ----------
    sales_data : list
        List of sales data records (dicts).
    column_name : str
        Name of the column to process.

    Returns
    -------
    float
        Total value of the column.
    """
    logger.info("Computing total value for column: %s", column_name)

    try:
        values = [record[column_name] for record in sales_data]
    except KeyError as error:
        msg = f"Column {column_name} not present in sales data."
        logger.error(msg)
        raise RuntimeError(msg) from error

    logger.debug("Total value: %0.2f", sum(values))
    return sum(values)


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
    totals = {}
    for record in sales_data:
        if record[group_column] in totals:
            totals[record[group_column]] += record[value_column]
        else:
            totals[record[group_column]] = record[value_column]

    # Get key corresponding to max value.
    best_key = max(totals, key=lambda key: totals[key])

    logger.debug("Best %s: %s.", group_column, best_key)
    logger.debug("Best %s: %0.2f.", value_column, totals[best_key])
    return best_key, totals[best_key]


def main():
    """Main program routine."""
    logger.info("Generating sales report for %s.", REPORT_DATE)
    sales_data = read_sales_data(SALES_PATH, REPORT_DATE)

    total_customers = count_unique(sales_data, "customer_id")
    total_sales = compute_total(sales_data, "total")
    total_products = compute_total(sales_data, "quantity")
    best_customer, best_customer_value = compute_best(
        sales_data, "customer_id", "total"
    )
    best_product, best_product_value = compute_best(sales_data, "product_id", "total")
    logger.info("Finished generating sales report.")

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
