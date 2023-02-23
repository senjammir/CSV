""" handle error checing using try and except
    change file to use death valley data"""



import csv
from datetime import datetime


infile = open("death_valley_2018_simple.csv",'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):  #enumerate works on a list
    print(index,column_header)

highs = [] # Y1
lows = []   # Y2
dates = []  #X1


for row in csvfile:

    try:
        high = int(row[4])
        low = int(row[5])
        thedate = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError as err:
        print(f"The missing data is {row[2]}")

    else:
        highs.append(high)
        lows.append(low)
        dates.append(thedate)

import matplotlib.pyplot as plt

fig = plt.figure()

plt.plot(dates, highs, c ='red', alpha = 0.5)
plt.plot(dates, lows, c="blue", alpha= 0.5)

plt.fill_between(dates, lows, highs, facecolor = 'blue', alpha=0.1)

plt.title("Daily Low and High Tempreture - 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Tempreture(F), fontsize=16")
plt.tick_params(axis="both",which="major",labelsize=16)

fig.autofmt_xdate()
plt.show()