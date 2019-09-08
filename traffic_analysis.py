import pandas as pd
import numpy as np

df = pd.read_csv('pd_collisions_datasd_v1.csv')
#Open dataframe with collision data

#TODO filter by year, month, day, hour
df = df.drop(['report_id',
              'police_beat',
              'address_pd_primary',
              'address_sfx_primary',
              'address_pd_intersecting',
              'address_name_intersecting',
              'violation_section',
              'violation_type',
              'charge_desc',
              'hit_run_lvl'], axis=1)
#dropping columns not needed to map the data

print(df.columns)
#confirming dropped columns with unwanted data

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


print(df.dtypes)
#confirms that all are object type before combining below

address_number = df['address_number_primary']
address_road = df['address_road_primary']
address_sfx = df['address_sfx_intersecting']
df['total_address'] = address_number + ' ' + address_road + ' ' + address_sfx
#combining columns into new column 'working_address'



print(df)
