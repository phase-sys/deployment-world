# PATTERN_MAX(100.00, 6, 2, 4, yyyy-mm-dd)
# (1000.00, 1, 1, 1, "2010-01-01")

import random, pandas, datetime

f = open("transaction_data.txt", "w")
date_data = []
sdate = datetime.date(2019, 1, 1)
edate = datetime.date(2021, 10, 9)

for a in pandas.date_range(sdate, edate - datetime.timedelta(days=1), freq='d').strftime('%Y-%m-%d'):
    date_data.append(a)

i = 0
while i < 1000:
    f.write("({0}, {1}, {2}, {3}, \"{4}\"),".format(random.randrange(100, 5001, 100), random.randrange(1,7), random.randrange(1,3), random.randrange(1,5), date_data[i]))
    i += 1

f.close()

f = open("transaction_data.txt", "r")
print(f.read())
f.close()