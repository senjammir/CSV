
import csv
from datetime import datetime
import matplotlib.pyplot as plt



infile = open("sitka_weather_2018_simple.csv",'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

TMAX_index = header_row.index('TMAX')
TMIN_index = header_row.index('TMIN')
DATE_index = header_row.index('DATE')
NAME_index = header_row.index('NAME')

highs1 = [] # Y1
lows1 = []   # Y2
dates1 = []  #X

for row in csvfile:
    highs1.append(int(row[TMAX_index]))
    lows1.append(int(row[TMIN_index]))
    thedate = datetime.strptime(row[DATE_index], '%Y-%m-%d')
    dates1.append(thedate)
    name1 = row[NAME_index]

infile = open("death_valley_2018_simple.csv",'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

TMAX_index = header_row.index('TMAX')
TMIN_index = header_row.index('TMIN')
DATE_index = header_row.index('DATE')
NAME_index = header_row.index('NAME')

highs2 = [] # Y1
lows2 = []   # Y2
dates2 = []  #X

for row in csvfile:

    try:
        high = int(row[TMAX_index])
        low = int(row[TMIN_index])
        thedate = datetime.strptime(row[DATE_index], '%Y-%m-%d')
    except ValueError as err:
        print(f"The missing data is {row[DATE_index]}")

    else:
        highs2.append(high)
        lows2.append(low)
        dates2.append(thedate)
        name2 = row[NAME_index]

fig = plt.figure()
plt.subplot(2,1,1)      #plt.subplot(no of rows, no of columns, index value)
plt.plot(dates1, highs1, c ='red', alpha = 0.5)
plt.plot(dates1, lows1, c="blue", alpha= 0.5)

plt.fill_between(dates1, lows1, highs1, facecolor = 'blue', alpha=0.1)

plt.title(name1)
plt.xlabel("")
plt.ylabel("")
plt.tick_params(axis="both",which="major",labelsize=16)
fig.autofmt_xdate()


plt.subplot(2,1,2)
plt.plot(dates2, highs2, c ='red', alpha = 0.5)
plt.plot(dates2, lows2, c="blue", alpha= 0.5)

plt.fill_between(dates2, lows2, highs2, facecolor = 'blue', alpha=0.1)

plt.title(name2)
plt.xlabel("")
plt.ylabel("")
plt.tick_params(axis="both",which="major",labelsize=16)
fig.autofmt_xdate()

plt.suptitle(f"Tempreture comparison between {name1} and {name2}", fontsize = 16)

plt.show()