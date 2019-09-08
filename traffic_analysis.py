import pandas as pd
import numpy as np

df = pd.read_csv('pd_collisions_datasd_v1.csv')
#Open dataframe with collision data

#print(df.columns)
df = df.drop(['report_id',
              'police_beat',
              'address_pd_primary',
              'address_sfx_primary',
              'address_pd_intersecting',
              'address_name_intersecting',
              'violation_section',
              'violation_type',
              'charge_desc'], axis=1)
#dropping columns not needed to map the data
#print(df.columns)
#confirming dropped columns with unwanted data

df = df.astype(str)
#cast all columns to type(str) for combining columns

#TODO fill NaN and empty with 0
hit_run_data = df['hit_run_lvl']
fatal = df['killed']

print(df.dtypes)

address_number = df['address_number_primary']
address_road = df['address_road_primary']
address_sfx = df['address_sfx_intersecting']
df['total_address'] = address_number + ' ' + address_road + ' ' + address_sfx
#combining columns into new column 'working_address'



print(df)

#print(df['address'])


#df['start_and_end'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
