import pandas as pd
import numpy as np
#import plotly.express as px
import matplotlib.pyplot as plt
#considering plotly instead of matplotlib
from geopy.geocoders import Nominatim
#allows conversion of street addresses to lat, long coords
import gmplot

df = pd.read_csv('pd_collisions_datasd_v1.csv')
#Open dataframe with collision data

#TODO filter by year, month, day, hour
df = df.drop(['police_beat',
              'address_pd_primary',
              'address_sfx_primary',
              'address_pd_intersecting',
              'address_name_intersecting',
              'violation_section',
              'violation_type',
              'charge_desc',
              'hit_run_lvl'], axis=1)
#dropping columns not needed to map the data

df['city'] = 'San Diego'
df['state'] = 'California'
df['state_ab'] = 'CA'
#adding San Diego as city for all addresses

df = df.astype(str)
#cast all columns to type(str) for combining columns

#TODO fill NaN and empty with 0
df = df.fillna(0)

df['date_time'] =  pd.to_datetime(df['date_time'])

df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['day'] = df['date_time'].dt.day
df['hour'] = df['date_time'].dt.hour
#adding columns for date_time graphing

most_common_year = df['year'].mode()
most_common_month = df['month'].mode()
most_common_day = df['day'].mode()
most_common_hour = df['hour'].mode()
avg_month_casualty = df.groupby(['year', 'month', 'killed'])
month_mean = avg_month_casualty.mean()
print(month_mean)

print('The most crashes happened in {}'.format(most_common_year))
print('The most crashes happened in {}'.format(most_common_month))
print('The most crashes happened in {}'.format(most_common_day))
print('The most crashes happened in {}'.format(most_common_hour))

df.set_index('date_time', inplace=True)
df.groupby('year')['killed'].count().plot()
plt.xlabel('Dates')
plt.show()
#plot collision data grouped by year and by month

#find count of unique crash records, grouped by year
"""grouped_months = df.groupby(['month'])
collision_data_count = grouped_months.count().plot()
plt.show()"""
#grouping by column and printing groups

#print(df.dtypes)
#confirms that all are object type before combining below

city = df['city']
state = df['state']
address_number = df['address_number_primary']
address_road = df['address_road_primary']
address_sfx = df['address_sfx_intersecting']
df['total_address'] = address_number + ' ' + address_road + ' ' + address_sfx + ', ' + city + ', ' + state
#combining columns into new column 'working_address'
print(df.shape)
#the Geocoder package could take an address and convert to lat, long
total_address = df['total_address']
geolocator = Nominatim(user_agent='sd-traffic-analysis')

def to_coordinates(address):
    try:
        location = geolocator.geocode(address)
        lats_longs.append(location)
        print((location.latitude), (location.longitude))
    except:
        print('Invalid address, moving on...')
    return lats_longs


lats_longs = []
for index, address in enumerate(total_address):
    to_coordinates(address)
    if index == 5:
        break
#for testing purposes, limiting to five lines

for location in lats_longs:
    with open('latitude_longitude.csv', 'a+') as file:
        file.write(str(location))


#TODO: once have lat, long plot the map
