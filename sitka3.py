""" change the file to include all the data for the year 2018
    change the title to daily and low high tempreture 2018
    extra low tempreture from the file and add to chart
    shade in the area between high and low"""



import csv
from datetime import datetime


infile = open("sitka_weather_2018_simple.csv",'r')
csvfile = csv.reader(infile)

header_row = next(csvfile)

for index, column_header in enumerate(header_row):  #enumerate works on a list
    print(index,column_header)

highs = [] # Y1
lows = []   # Y2
dates = []  #X1



for row in csvfile:
    highs.append(int(row[5]))
    lows.append(int(row[6]))
    thedate = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(thedate)

print(highs)
print(lows)

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

"""How to do subplots"""

plt.subplot(2,1,1)      #plt.subplot(no of rows, no of columns, index value)
plt.plot(dates,highs,c='red')
plt.title('Highs')

plt.subplot(2,1,2)
plt.plot(dates,lows, c='blue')
plt.title('Lows')

plt.suptitle("Highs and lows of Sitka, Alaska")

plt.show()