import numpy as np
import pandas as pd

df = pd.read_csv('data_mining.csv')

df['bitcoin'] = np.log(df['bitcoin'])
df['bitcoin_buy'] = np.log(df['bitcoin_buy'])
df['bitcoin_mining'] = np.log(df['bitcoin_mining'])
df['bitcoin_price'] = np.log(df['bitcoin_price'])
df['blockchain'] = np.log(df['blockchain'])
df['value'] = np.log(df['value'])
df['unique'] = np.log(df['unique'])
df['trans_volume'] = np.log(df['trans_volume'])
df['revenue'] = np.log(df['revenue'])
df['trade_volume'] = np.log(df['trade_volume'])
df['market_cap'] = np.log(df['market_cap'])
df['value_1'] = np.log(df['value_1'])
df['value_2'] = np.log(df['value_2'])
df['value_3'] = np.log(df['value_3'])
df['value_4'] = np.log(df['value_4'])
df['value_5'] = np.log(df['value_5'])
df['value_6'] = np.log(df['value_6'])
df['value_7'] = np.log(df['value_7'])
df['value_8'] = np.log(df['value_8'])
df['value_tomorrow'] = np.log(df['value_tomorrow'])

df