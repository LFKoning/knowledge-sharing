import random

import pandas as pd
import scipy.stats as stats

from faker import Faker

fkr = Faker("nl_NL")
fkr.seed_instance(1234)


def record_factory():
    """Generator for fake sales records."""

    pid = 0

    while True:
        pid += 1
        gender = random.choice(["male", "female"])
        if gender == "male":
            first_name = fkr.first_name_male()
        else:
            first_name = fkr.first_name_female()

        data = {
            "id": pid,
            "first_name": first_name,
            "last_name": fkr.last_name(),
            "birthdate": fkr.date_between(start_date="-30y", end_date="-18y"),
            "gender": gender,
            "city": random.choice(
                ["Amsterdam", "Den Haag", "Eindhoven", "Utrecht", "Rotterdam"]
            ),
            "orders": 1 + int(stats.expon(0.1).rvs() * 3),
            "order_amount": 1 + int(stats.expon(0.1).rvs() * 20),
            "opt_in": random.choice([True, False]),
        }

        yield data


def list_methods(cls, public_only=True, summary=True, docstring=False):
    """Extract method names and docstrings from a class."""

    methods = []
    for method_name in dir(cls):

        # Skip private / protected / dunder methods
        if public_only and method_name.startswith("_"):
            continue
        elif method_name.startswith("__"):
            continue

        rec = {"name": method_name}

        if summary or docstring:
            method = getattr(cls, method_name)

            if hasattr(method, "__doc__"):

                doc = method.__doc__
                if doc:
                    doc = doc.strip()
                    rec["summary"] = doc.splitlines()[0]
                    if docstring:
                        rec["docstring"] = doc

        methods.append(rec)

    return pd.DataFrame(methods)
