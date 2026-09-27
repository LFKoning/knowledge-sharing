"""Demonstrate exception handling."""


def compute_mean(values):
    """Compute mean of a list of values."""
    return sum(values) / len(values)


def main():
    """Main program routine."""
    ages = [33, 45, 22, None, 18]
    compute_mean(ages)


if __name__ == "__main__":
    main()
