import pandas as pd
import numpy as np

raw_data = pd.read_csv('POWER_SinglePoint_Daily_20150101_20200101.csv', skiprows = 20)
raw_data = raw_data.drop(['CLRSKY_SFC_SW_DWN'], axis=1)

print(raw_data.corr())