import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


elev_data = pd.read_csv('./Fahrtdaten.csv')

elev_data['ts'] = pd.to_datetime(elev_data['ts'], unit='ms')
elev_data['date'] = elev_data['ts'].dt.date

elev_data['distance'] = elev_data['distance'].abs()


rides_per_day = elev_data.groupby('date').size()

days_with_least_num_of_rides = rides_per_day [rides_per_day < 25]
print(days_with_least_num_of_rides.index)

day_with_most_rides = rides_per_day.idxmax()

most_rides = rides_per_day.max()

print(f"Day with most rides: {day_with_most_rides} with {most_rides} rides")


plt.figure(figsize=(15,6))
plt.bar(rides_per_day.index, rides_per_day)
plt.title('Rides per Day')
plt.xlabel("Date")
plt.ylabel("Number of trips")
plt.show()


# Irrehularities Analysis 

#max_distance = elev_data['distance'].max()
#print(max_distance)
#plt.hist(elev_data['distance'], bins=50)
#plt.show()
