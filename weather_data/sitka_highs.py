from pathlib import Path
import csv 

import matplotlib.pyplot as plt 

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
#plot the high temperatures directly from the csv file
plt.style.use("ggplot")
fig, ax = plt.subplots()    
ax.set_title("Daily high temperatures - 2021", fontsize=16)
ax.set_xlabel("", fontsize=14)
ax.set_ylabel("Temperature (F)", fontsize=14)
ax.tick_params(axis='both', which='major', labelsize=14)
plt.show()

#for index, column_header in enumerate(header_row):
    #print(index, column_header)

#Extract high temperatures
#highs = []
#for row in reader:
    #high = int(row[4])
    #highs.append(high)

#print(len(highs))
