import datetime as dt

# Read data
records = []
file = open("../../0_data/sales/transactions.csv", "r")
header = next(file).strip().split(",")
for line in file:
    values = line.strip().split(",")
    record = {col: val for col, val in zip(header, values)}

    record["aantal"] = int(record["aantal"])
    record["prijs"] = float(record["prijs"])
    record["prijs_totaal"] = float(record["prijs_totaal"])
    record["verpakking"] = float(record["verpakking"])

    records.append(record)

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

# Sales per customer and item
csls = {}
psls = {}
for record in records:
    if record["datum"] != dt.datetime.strptime(date, "%Y-%m-%d"):
        continue

    if record["klant_id"] in csls:
        csls[record["klant_id"]] += record["prijs_totaal"]
    else:
        csls[record["klant_id"]] = record["prijs_totaal"]

    if record["product"] in psls:
        psls[record["product"]] += record["prijs_totaal"]
    else:
        psls[record["product"]] = record["prijs_totaal"]


# Get max values
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
print(f"Aantal klanten:                      {tc}")
print(f"Totaal waarde:                       {round(ts, 2)}")
print(f"Totaal producten                     {ti}")
print("------------------------------------------")
print(f"Gemiddeld bedrag per klant:          {round(ts / tc, 2)}")
print(f"Gemiddeld producten per klant:       {round(ti / tc, 2)}")
print("------------------------------------------")
print(f"Beste klant:                         {bc}")
print(f"Beste klant waarde:                  {round(bcv, 2)}")
print(f"Beste product                        {bp}")
print(f"Beste product waarde:                {round(bpv, 2)}")
print("==========================================")
