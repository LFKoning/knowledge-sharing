import datetime as dt

# Read data
records = []
file = open("../../0_data/sales/transactions.csv", "r")
header = next(file).strip().split(",")
for line in file:
    values = line.strip().split(",")

    record = {}
    for i, c in enumerate(header):
        record[c] = values[i]

    record["quantity"] = int(record["quantity"])
    record["quantity"] = int(record["line_nr"])
    record["price"] = float(record["price"])
    record["total"] = float(record["total"])

    records.append(record)

# Fix dates
for record in records:
    record["transaction_date"] = dt.datetime.strptime(
        record["transaction_date"], "%Y-%m-%d"
    )

# Set report date
date = "2023-01-15"

# Compute totals for the day
ts = 0
ti = 0
for record in records:
    if record["transaction_date"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue
    ts += record["total"]
    ti += record["quantity"]

# Compute number of customers
cust = []
tc = 0
for record in records:
    if record["transaction_date"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue
    if record["customer_id"] in cust:
        continue
    tc += 1
    cust.append(record["customer_id"])

# Sales per customer and product
csls = {}
psls = {}
for record in records:
    if record["transaction_date"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue

    if record["customer_id"] in csls:
        csls[record["customer_id"]] += record["total"]
    else:
        csls[record["customer_id"]] = record["total"]

    if record["product_id"] in psls:
        psls[record["product_id"]] += record["total"]
    else:
        psls[record["product_id"]] = record["total"]


# Get best sellers
bc = ""
bcv = 0
for c, t in csls.items():
    if t > bcv:
        bc = c
        bcv = t

bp = ""
bpv = 0
for p, t in psls.items():
    if t > bpv:
        bp = p
        bpv = t


# Print report
print("==========================================")
print(f"Report for:                           {date}")
print("------------------------------------------")
print(f"Aantal klanten:                       {tc}")
print(f"Totaal waarde:                        {ts}")
print(f"Totaal producten                      {ti}")
print("------------------------------------------")
print(f"Gemiddeld bedrag per klant:           {ts / tc}")
print(f"Gemiddeld producten per klant:        {ti / tc}")
print("------------------------------------------")
print(f"Beste klant:                          {bc}")
print(f"Beste klant waarde:                   {bcv}")
print(f"Beste product                         {bp}")
print(f"Beste product waarde:                 {bpv}")
print("==========================================")
