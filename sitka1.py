

import csv
from datetime import datetime 

infile = open("sitka_weather_07-2018_simple.csv",'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):  #enumerate works on a list
    print(index,column_header)

highs = []
dates = []

mydate = datetime.strptime('2018-07-01','%Y-%m-%d')



for row in csvfile:
    highs.append(int(row[5]))
    thedate = datetime.strptime(row[2],'%Y-%m-%d')
    dates.append(thedate)

print(highs)

import matplotlib.pyplot as plt

fig = plt.figure()  #allows us to use a specific function to allow the dates to be slanted

plt.plot(dates, highs, c='blue') # x and followed by y
plt.title("Daily High Tempreture for Sitka Alaska, July 2018", fontsize = 16)
plt.xlabel("")
plt.ylabel("Tempreture(F), fontsize=16")
plt.tick_params(axis="both",which="major",labelsize=16)
fig.autofmt_xdate()

plt.show()
