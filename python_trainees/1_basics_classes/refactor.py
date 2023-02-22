import datetime as dt

# Read data
records = []
file = open("../data/sales_data.csv")
for line in file:
    records.append(line.split(","))

# Fix dates
for record in records:
    record["datum"] = dt.datetime.strptime(record["datum"], "%Y-%m-%d")

# Set report date
date = "2023-1-15"

# Compute totals for the day
ts = 0
ti = 0
for record in records:
    if record["datum"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue
    ts += record["prijs_totaal"]
    ti += record["aantal"]

# Compute number of customers
cust = []
tc = 0
for record in records:
    if record["datum"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue
    if record["klant_id"] in cust:
        continue
    tc += 1
    cust.append(record["klant_id"])


# Sales and items per customer
cs = {}
ci = {}
for record in records:
    if record["datum"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue
    if record["klant_id"] in cs:
        cs[record["klant_id"]] += record["totaal_prijs"]
        ci[record["klant_id"]] += record["aantal"]
    else:
        cs[record["klant_id"]] = record["totaal_prijs"]
        ci[record["klant_id"]] = record["aantal"]

# Compute means
mcs = 0
for cust, total in cs.items():
    mcs += total
mcs = mcs / len(mcs)

mci = 0
for cust, items in ci.items():
    mci += items
mci = mci / len(mcs)

# Print report
print("Report for:     {date}")
print("----------------------")
print("Aantal klanten:   {ts}")
print("Totaal waarde:    {ts}")
print("Totaal items:     {ti}")