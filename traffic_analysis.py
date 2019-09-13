import pandas as pd
import numpy as np
#import plotly.express as px
import matplotlib.pyplot as plt
#considering plotly instead of matplotlib
from geopy.geocoders import Nominatim


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

fatal = df['killed']
#to be used for conditional analysis

df['year'] = df['date_time'].dt.year
df['month'] = df['date_time'].dt.month
df['day'] = df['date_time'].dt.day
df['hour'] = df['date_time'].dt.hour
#adding columns for date_time graphing

most_common_year = df['year'].mode()
most_common_month = df['month'].mode()
most_common_day = df['day'].mode()
most_common_hour = df['hour'].mode()

print('The most crashes happened in {}'.format(most_common_year))
print('The most crashes happened in {}'.format(most_common_month))
print('The most crashes happened in {}'.format(most_common_day))
print('The most crashes happened in {}'.format(most_common_hour))

plt.figure(1)
df.groupby('year')['date_time'].nunique().plot(kind='bar')

plt.figure(2)
df.groupby('month')['date_time'].nunique().plot(kind='bar')

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

#the Geocoder package could take an address and convert to lat, long
total_address = df['total_address']
geolocator = Nominatim(user_agent='sd-traffic-analysis')
for address in total_address:
    try:
        location = geolocator.geocode(address)
        print((location.latitude, location.longitude))
    except AttributeError:
        print('Invalid address, moving on...')
#TODO: once have lat, long plot the map
