# CHECK ME:
# https://stackoverflow.com/questions/59882714/python-generating-a-list-of-dates-between-two-dates
# https://www.w3schools.com/python/python_file_handling.asp
# https://www.w3schools.com/python/python_string_formatting.asp
# https://www.w3schools.com/python/python_datetime.asp

import random, pandas, datetime

f = open("budget_data.txt", "w")
date_data = []
sdate = datetime.date(2019, 1, 1)
edate = datetime.date(2021, 10, 9)

for a in pandas.date_range(sdate, edate - datetime.timedelta(days=1), freq='d').strftime('%Y-%m-%d'):
    date_data.append(a)

i = 0
while i < 1000:
    f.write("({0}, {1}, {2}, {3}, \"{4}\"),".format(random.randrange(100, 5001, 100), random.randrange(1,5), random.randrange(1,5), random.randrange(1,6), date_data[i]))
    i += 1

f.close()

f = open("budget_data.txt", "r")
print(f.read())
f.close()