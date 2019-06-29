from datetime import datetime, timedelta
from pytrends.request import TrendReq
import pandas as pd
import os

maxstep = 269
overlap = 40
step    = maxstep - overlap + 1
start_date = datetime(2012, 1, 1).date()
old_date = datetime(2019, 1, 1).date()
# Login to Google. Only need to run this once, the rest of requests will use the same session.
pytrend = TrendReq()
# List of searches ***OBS: limit list 5 elements
kw_list = ['bitcoin', 'blockchain', 'bitcoin price', 'bitcoin buy', 'bitcoin mining']
# Go back in time
new_date = old_date - timedelta(days=step)
# Create new timeframe for which we download data
timeframe = new_date.strftime('%Y-%m-%d')+' '+old_date.strftime('%Y-%m-%d')
pytrend.build_payload(kw_list=kw_list, timeframe = timeframe)
interest_over_time_df = pytrend.interest_over_time()

## RUN ITERATIONS
while new_date>start_date:
    old_date = new_date + timedelta(days=overlap-1)
    new_date = new_date - timedelta(days=step)
    
    # If we went past our start_date, use it instead
    if new_date < start_date:
        new_date = start_date

    # New timeframe
    timeframe = new_date.strftime('%Y-%m-%d')+' '+old_date.strftime('%Y-%m-%d')
    # Download data
    pytrend.build_payload(kw_list=kw_list, timeframe = timeframe)
    temp_df = pytrend.interest_over_time()
    if (temp_df.empty):
        raise ValueError('Google sent back an empty dataframe.')
    # Renormalize the dataset and drop last line
    for kw in kw_list:
        beg = new_date
        end = old_date - timedelta(days=1)
        # Since we might encounter zeros, we loop over the overlap until we find a non-zero element
        for t in range(1,overlap+1):
            if temp_df[kw].iloc[-t] != 0:
                scaling = interest_over_time_df[kw].iloc[t-1]/temp_df[kw].iloc[-t]
                break
            elif t == overlap:
                print('Did not find non-zero overlap, set scaling to zero! Increase Overlap!')
                scaling = 0
        # Apply scaling
        temp_df.loc[beg:end,kw]=temp_df.loc[beg:end,kw]*scaling
    interest_over_time_df = pd.concat([temp_df[:-overlap],interest_over_time_df])

# Save dataset
interest_over_time_df.to_csv('trends_data.csv')
