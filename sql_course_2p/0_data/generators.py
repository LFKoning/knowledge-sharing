"""Module for generating dummy SQLite databases."""

import sqlite3

from sales_generator import SalesGenerator

# Sales generator parameters.
N_YEARS = 5
FINAL_YEAR = -1
N_CUSTOMERS = 250
DAILY_TRANSACTIONS = 10

# Database files.
SALES_DB = "sales_data.db"
JOINS_DB = "join_types.db"
CUSTOMER_DB = "customer.db"


def generate_sales() -> None:
    """Generate a dummy database with sales data."""

    # Set up SQLite and Faker.
    db = sqlite3.connect(SALES_DB)
    cursor = db.cursor()

    # Initialize database tables.
    with open("sales_tables.sql", "r", encoding="utf-8") as create_sql:
        cursor.executescript(create_sql.read())

    generator = SalesGenerator(n_years=N_YEARS)

    # First generate customers.
    customer_df = generator.generate_customers(N_CUSTOMERS)
    customer_df.to_sql("Klanten", db, index=False, if_exists="append")

    # Then generate products.
    product_df = generator.generate_products()
    product_df.to_sql("Producten", db, index=False, if_exists="append")

    # Finally generate transactions.
    transaction_df = generator.generate_transactions(
        customer_df, product_df, DAILY_TRANSACTIONS
    )
    transaction_df.to_sql("Transacties", db, index=False, if_exists="append")

    db.commit()
    db.close()


def generate_joins() -> None:
    """Generate a dummy database for join types."""
    db = sqlite3.connect(JOINS_DB)
    cursor = db.cursor()

    with open("join_types.sql", "r", encoding="utf-8") as joins_sql:
        cursor.executescript(joins_sql.read())

    db.commit()
    db.close()


def generate_customers() -> None:
    """Generate a dummy database with customer data."""
    db = sqlite3.connect(CUSTOMER_DB)
    cursor = db.cursor()

    with open("customers.sql", "r", encoding="utf-8") as customers_sql:
        cursor.executescript(customers_sql.read())

    db.commit()
    db.close()


def main() -> None:
    """Main program routine."""

    print("Generating sales database...")
    generate_sales()

    print("Generating JOINs database...")
    generate_joins()

    print("Generating customer database...")
    generate_customers()

    print("All databases generated successfully.")


if __name__ == "__main__":
    main()
