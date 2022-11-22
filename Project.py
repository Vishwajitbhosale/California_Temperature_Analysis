import numpy as np
import pandas as pd
import matplotlib as mlb
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

geodata = pd.read_csv("geo-data.csv")
Zip10001 = pd.read_csv("10001 2021-01-01 to 2021-12-31.csv")
Zip10006 = pd.read_csv("10006 2021-01-01 to 2021-12-31.csv")
Zip10011 = pd.read_csv("10011 2021-01-01 to 2021-12-31.csv")
Zip10017 = pd.read_csv("10017 2021-01-01 to 2021-12-31.csv")
Zip94017 = pd.read_csv("94017 2021-01-01 to 2021-12-31.csv")
Zip94105 = pd.read_csv("94105 2021-01-01 to 2021-12-31.csv")
Zip94127_94132 = pd.read_csv("94127&94132  2021-01-01 to 2021-12-31.csv")

monthslabel = ["jan", "feb", "march", "apr", "may", "june", "jul", "aug", "sep", "oct", "nov", "dec"]

# print(type(Zip10001))
geodata["zipcode"] = geodata["zipcode"].astype(str)
Zip10001["name"] = Zip10001["name"].astype(str)
NewDF = pd.merge(geodata, Zip10001, left_on="zipcode", right_on="name")
NewDF["datetime"] = NewDF["datetime"].str.slice(5, 7)
Monthlymax1 = list(NewDF.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg1 = list(NewDF.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg1, color="red")
plt.ylabel("Temperature")
plt.xlabel("Months")

print(Monthlymax1)
yearmax = []
Zip10006["name"] = Zip10006["name"].astype(str)
NewDF1 = pd.merge(geodata, Zip10006, left_on="zipcode", right_on="name")
NewDF1["datetime"] = NewDF1["datetime"].str.slice(5, 7)
Monthlymax2 = list(NewDF1.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg2 = list(NewDF1.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg2, '-.', color="blue")
print(Monthlymax2)

Zip10011["name"] = Zip10011["name"].astype(str)
NewDF2 = pd.merge(geodata, Zip10011, left_on="zipcode", right_on="name")
NewDF2["datetime"] = NewDF2["datetime"].str.slice(5, 7)
Monthlymax3 = list(NewDF2.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg3 = list(NewDF2.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg3, '-.', color="orange")
print(Monthlymax3)

Zip10017["name"] = Zip10017["name"].astype(str)
NewDF4 = pd.merge(geodata, Zip10017, left_on="zipcode", right_on="name")
NewDF4["datetime"] = NewDF4["datetime"].str.slice(5, 7)
Monthlymax4 = list(NewDF4.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg5 = list(NewDF4.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg5, '-.', color="black")
print(Monthlymax4)

Zip94105["name"] = Zip94105["name"].astype(str)
NewDF5 = pd.merge(geodata, Zip94105, left_on="zipcode", right_on="name")
NewDF5["datetime"] = NewDF5["datetime"].str.slice(5, 7)
Monthlymax5 = list(NewDF5.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg6 = list(NewDF5.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg6, '-.', color="green")
print(Monthlymax5)

Zip94017["name"] = Zip94017["name"].astype(str)
NewDF6 = pd.merge(geodata, Zip94017, left_on="zipcode", right_on="name")
NewDF6["datetime"] = NewDF6["datetime"].str.slice(5, 7)
Monthlymax6 = list(NewDF6.groupby("datetime").max("tempmax")["tempmax"])
print(max(NewDF6["tempmax"]))
Monthlavg7 = list(NewDF6.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg7, '-.', color="gray")

Zip94127_94132["name"] = Zip94127_94132["name"].astype(str)
NewDF7 = pd.merge(geodata, Zip94127_94132, left_on="zipcode", right_on="name")
NewDF7["datetime"] = NewDF7["datetime"].str.slice(5, 7)

NewDF8 = NewDF7.where(NewDF7["name"] == "94127")
NewDF9 = NewDF7.where(NewDF7["name"] == "94132")

Monthlymax7 = list(NewDF8.groupby("datetime").max("tempmax")["tempmax"])
print(max(NewDF8["tempmax"]))
Monthlavg8 = list(NewDF8.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg8, '-.', color="olive")

Monthlymax8 = list(NewDF9.groupby("datetime").max("tempmax")["tempmax"])
Monthlavg9 = list(NewDF9.groupby("datetime").mean("tempmax")["tempmax"])
plt.plot(monthslabel, Monthlavg9, '-.', color="brown")


plt.legend(["10001", "10006", "10011", "10017", "94105", "94017", "94127", "94132"])

fig, ax = plt.subplots()
ax.set_ylabel("Temperature")
ax.set_xlabel("Months")

ax.bar(monthslabel, Monthlymax1, label="10001")
ax.bar(monthslabel, Monthlymax2, bottom=Monthlymax1, label="10006")
ax.bar(monthslabel, Monthlymax3, bottom=np.array(Monthlymax2) + np.array(Monthlymax1), label="10011")
ax.bar(monthslabel, Monthlymax4, bottom=np.array(Monthlymax3) + np.array(Monthlymax2) + np.array(Monthlymax1),
       label="10017")
ax.bar(monthslabel, Monthlymax5,
       bottom=np.array(Monthlymax4) + np.array(Monthlymax3) + np.array(Monthlymax2) + np.array(Monthlymax1),
       label="94105")
ax.bar(monthslabel, Monthlymax6,
       bottom=np.array(Monthlymax5) + np.array(Monthlymax4) + np.array(Monthlymax3) + np.array(Monthlymax2) + np.array(
           Monthlymax1), label="94017")
ax.bar(monthslabel, Monthlymax7,
       bottom=np.array(Monthlymax6) + np.array(Monthlymax5) + np.array(Monthlymax4) + np.array(Monthlymax3) + np.array(
           Monthlymax2) + np.array(Monthlymax1), label="94127")
ax.bar(monthslabel, Monthlymax8,
       bottom=np.array(Monthlymax7) + np.array(Monthlymax6) + np.array(Monthlymax5) + np.array(Monthlymax4) + np.array(
           Monthlymax3) + np.array(Monthlymax2) + np.array(Monthlymax1), label="94132")
ax.legend(loc="upper right")
plt.show()

import pandas as pd

#cities = pd.read_csv("data.csv")
data={"zip":[94127,94017,94132],
      "latd":[37.732366,37.381144,37.7205880],
      "longd":[-122.457441,-122.334825,-122.47682344],
      "area_total_km2":[1.77,1,3.11],
      "Temp":[max(NewDF6["tempmax"]),max(NewDF8["tempmax"]),87.7]}

cities = pd.DataFrame(data)

lat = cities['latd']
lon = cities['longd'].values
Temp = cities['Temp'].values
area = cities['area_total_km2'].values

# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc',  # , resolution='h'
            lat_0=42, lon_0=-122,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

y=[20*4**n for n in range(len(Temp))]
print(y)
m.scatter(lon, lat, latlon=True,
          c=np.array(Temp)*50, s=y,
          cmap='Reds', alpha=1)

plt.clim(3, 7)

plt.scatter(lon,lat, c=np.array(Temp)*50, alpha=0.5, s=y,
               label=str(area))

plt.show()
