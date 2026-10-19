"""Module for generating dummy SQLite databases."""

import sqlite3
from pathlib import Path

from sales_generator import SalesGenerator

# Sales generator parameters.
N_YEARS = 5
FINAL_YEAR = -1
N_CUSTOMERS = 250
DAILY_TRANSACTIONS = 10

# Data folder
DATA_PATH = "../0_data"

# Database files.
SALES_DB = "sales_data.db"
JOINS_DB = "join_types.db"
CUSTOMER_DB = "customer.db"


def generate_sales() -> None:
    """Generate a dummy database with sales data."""

    # Set up SQLite and Faker.
    sales_path = Path(DATA_PATH) / Path(SALES_DB)
    db = sqlite3.connect(sales_path)
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
    joins_path = Path(DATA_PATH) / Path(JOINS_DB)
    db = sqlite3.connect(joins_path)
    cursor = db.cursor()

    with open("join_types.sql", "r", encoding="utf-8") as joins_sql:
        cursor.executescript(joins_sql.read())

    db.commit()
    db.close()


def generate_customers() -> None:
    """Generate a dummy database with customer data."""
    customer_path = Path(DATA_PATH) / Path(CUSTOMER_DB)
    db = sqlite3.connect(customer_path)
    cursor = db.cursor()

    with open("customers.sql", "r", encoding="utf-8") as customers_sql:
        cursor.executescript(customers_sql.read())

    db.commit()
    db.close()


def main() -> None:
    """Main program routine."""

    print("Creating data folder...")
    Path(DATA_PATH).mkdir(parents=True, exist_ok=True)

    print("Generating sales database...")
    generate_sales()

    print("Generating JOINs database...")
    generate_joins()

    print("Generating customer database...")
    generate_customers()

    print("All databases generated successfully.")


if __name__ == "__main__":
    main()
