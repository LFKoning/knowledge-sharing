"""Module for generating a dummy sales databases."""

import datetime as dt
import random
import unicodedata

import pandas as pd
from faker import Faker


class SalesGenerator:
    """Class for generating dummy sales data.

    Parameters
    ----------
    n_years : int, default=5
        Number of years to generatre data for.
    final_year : int, default=-1
        Final year to generate data for, relative to the current year.
    """

    domains = (
        "gmail.com",
        "hotmail.com",
        "outlook.com",
        "kpn.nl",
        "ziggo.nl",
    )

    def __init__(self, n_years: int = 5, final_year: int = -1) -> None:
        self.faker = Faker("nl_NL")

        final_year = dt.datetime.now(dt.UTC).year + final_year
        first_year = final_year - n_years

        self.start_dt = dt.datetime(first_year, 1, 1, tzinfo=dt.UTC)
        self.end_dt = dt.datetime(final_year, 12, 31, tzinfo=dt.UTC)

    @staticmethod
    def normalize(value: str) -> str:
        """Unicode normalize a string to ASCII."""
        return unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()

    def fake_mail(self, name: str) -> str:
        """Generate a fake email address based on a name."""
        domain = random.choice(self.domains)
        clean_name = SalesGenerator.normalize(name.lower().replace(" ", "."))
        return f"{clean_name}@{domain}"

    def generate_customers(self, n_customers: int) -> pd.DataFrame:
        """Generate fake customer data."""
        customers = []

        for _ in range(n_customers):
            name = self.faker.unique.name().split("-", 1)[0]
            address = self.faker.unique.address().split("\n")

            customers.append(
                {
                    "KlantId": self.faker.unique.bothify(text="CST-#####"),
                    "Naam": name,
                    "Email": self.fake_mail(name),
                    "Geboortedatum": self.faker.date_between("-80y", "-18y"),
                    "Adres": address[0],
                    "Postcode": address[1],
                    "Stad": address[2],
                    "Aangemaakt": self.faker.date_between(self.start_dt, self.end_dt),
                }
            )

        return pd.DataFrame(customers)

    def generate_products(self) -> pd.DataFrame:
        """Generate fake product data."""
        products = pd.read_csv("sales_products.csv")
        product_ids = [
            self.faker.unique.bothify(text="PRD-#####") for _ in range(len(products))
        ]
        products = products.assign(ProductId=product_ids)
        return products

    def generate_transactions(
        self, customer_df: pd.DataFrame, product_df: pd.DataFrame, n_daily: int
    ) -> pd.DataFrame:
        """Generate fake transaction data."""
        transactions = []
        day = self.start_dt
        while day <= self.end_dt:

            count = max(0, int(random.gauss(n_daily, 2)))
            for _ in range(count):
                customer_id = customer_df.sample(1).iloc[0, 0]
                transaction_id = self.faker.unique.bothify(text="TX-######")
                datetime = day + dt.timedelta(
                    seconds=random.randrange(9 * 3600, 18 * 3600)
                )

                for line_nr in range(random.randint(1, 5)):
                    product = product_df.sample(1)
                    transaction = {
                        "TransactieId": transaction_id,
                        "KlantId": customer_id,
                        "ProductId": product["ProductId"].iloc[0],
                        "DatumTijd": datetime.strftime("%Y-%m-%d %H:%M:%S"),
                        "RegelNummer": line_nr + 1,
                        "Aantal": round(random.lognormvariate(0.3, 0.4)),
                        "Prijs": product["Prijs"].iloc[0],
                    }

                    transactions.append(transaction)

            day += dt.timedelta(days=1)

        return pd.DataFrame(transactions)
