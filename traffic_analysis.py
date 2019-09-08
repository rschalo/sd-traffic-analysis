import pandas as pd
import numpy as np

df = pd.read_csv('pd_collisions_datasd_v1.csv')
#Open dataframe with collision data
print(df.columns)
df = df.drop(['violation_section', 'violation_type', 'charge_desc'], axis=1)
#dropping columns with unwanted data
print(df.columns)
