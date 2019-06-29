import pandas as pd
import quandl

## Requests to quandl
dfPrices = quandl.get("BCHAIN/MKPRU", start_date="2012-01-01", end_date="2018-12-31")
dfUnique = quandl.get("BCHAIN/NADDU", start_date="2012-01-01", end_date="2018-12-31")
dfTransactionVolume = quandl.get("BCHAIN/MWTRV", start_date="2012-01-01", end_date="2018-12-31")
dfRevenue = quandl.get("BCHAIN/MIREV", start_date="2012-01-01", end_date="2018-12-31")
dfTradeVolume = quandl.get("BCHAIN/TRVOU", start_date="2012-01-01", end_date="2018-12-31")
dfMarketCap = quandl.get("BCHAIN/MKTCP", start_date="2012-01-01", end_date="2018-12-31")

# Converting data to list
listPrices = dfPrices['Value'].tolist()
listUniques = dfUnique['Value'].tolist()
listTransactions = dfTransactionVolume['Value'].tolist()
listRevenue = dfRevenue['Value'].tolist()
listTrade = dfTradeVolume['Value'].tolist()
listMarketCap = dfMarketCap['Value'].tolist()

# Creating Dataframe
dfBitcoin = pd.DataFrame(columns=['date', 'value', 'unique', 'transVolume', 'revenue', 'tradeVolume', 'marketCap'])
dfBitcoin['date'] = dfPrices.index
dfBitcoin['value'] = listPrices
dfBitcoin['unique'] = listUniques
dfBitcoin['transVolume'] = listTransactions
dfBitcoin['revenue'] = listRevenue
dfBitcoin['tradeVolume'] = listTrade
dfBitcoin['marketCap'] = listMarketCap

# Export data
dfBitcoin.to_csv('bitcoin_data.csv')


