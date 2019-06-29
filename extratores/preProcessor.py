import pandas as pd

#### ___ functions
def classifier(data):
    
    def inputChange(cols):
        change = cols[0]

        if change <= 0:
            return 0
        else:
            return 1
    
    def classifiChange(cols):
        classe = "" 
        change = cols[0]

        if change >= 0 and change < 3:
            classe = 'up1' 
        if change >= 3 and change < 6:
            classe = 'up2'
        if change >= 6 and change < 9:
            classe = 'up3'
        if change >= 9:
            classe = 'up4'
        if change < 0 and change > -2:
            classe = 'down1'
        if change <= -2 and change > -4:
            classe = 'down2'
        if change <= -4 and change > -6:
            classe = 'down3'
        if change <= -6:
            classe = 'down4'

        return classe

    data['down_up'] = data[['change']].apply(inputChange,axis=1)
    data['class_change_tomorrow'] = data[['change_tomorrow']].apply(classifiChange,axis=1)
    data['class_change'] = data[['change']].apply(classifiChange,axis=1)

    return data
####

print("... START DATA PRE PROCESSING")

# Carregando os dados das fontes originais
dfBitcoin = pd.read_csv('bitcoin_data.csv')
dfTrends = pd.read_csv('trends_data.csv')

dfDataMining = pd.DataFrame(columns=['date', 'bitcoin', 'bitcoin_buy', 'bitcoin_mining', 'bitcoin_price','blockchain', 
                                    'value', 'unique', 'trans_volume', 'revenue', 'trade_volume', 'market_cap', 
                                    'value_1', 'value_2', 'value_3', 'value_4', 'value_5', 'value_6', 'value_7', 'value_8', 
                                    'change', 'change_1', 'change_2', 'change_3', 'change_4', 'change_5', 'down_up', 'value_tomorrow', 
                                    'change_tomorrow', 'class_change_tomorrow', 'change_bitcoin', 'change_unique', 'change_revenue',
                                    'change_trade_volume', 'change_market_cap'])


# Dados brutos sem necessidade de pré-processamento
dfDataMining['date'] = dfTrends['date']
dfDataMining['bitcoin'] = dfTrends['bitcoin']
dfDataMining['bitcoin_buy'] = dfTrends['bitcoin buy']
dfDataMining['bitcoin_mining'] = dfTrends['bitcoin mining']
dfDataMining['bitcoin_price'] = dfTrends['bitcoin price']
dfDataMining['blockchain'] = dfTrends['blockchain']
dfDataMining['value'] = dfBitcoin['value']
dfDataMining['unique'] = dfBitcoin['unique']
dfDataMining['trans_volume'] = dfBitcoin['transVolume']
dfDataMining['revenue'] = dfBitcoin['revenue']
dfDataMining['trade_volume'] = dfBitcoin['tradeVolume']
dfDataMining['market_cap'] = dfBitcoin['marketCap']


# Pré processamento dos dados
i = 0
while i < len(dfDataMining):
    if i == len(dfDataMining) - 1:
        dfDataMining['value_tomorrow'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['change_tomorrow'].iloc[i] = 0
    else:
        dfDataMining['value_tomorrow'].iloc[i] = dfDataMining['value'].iloc[i+1]
        dfDataMining['change_tomorrow'].iloc[i] = (dfDataMining['value_tomorrow'].iloc[i] * 100 / dfDataMining['value'].iloc[i]) - 100

    if i == 0:
        dfDataMining['change_bitcoin'].iloc[i] = 0
        dfDataMining['change_unique'].iloc[i] = 0
        dfDataMining['change_revenue'].iloc[i] = 0
        dfDataMining['change_trade_volume'].iloc[i] = 0
        dfDataMining['change_market_cap'].iloc[i] = 0
        dfDataMining['change'].iloc[i] = 0
        dfDataMining['change_1'].iloc[i] = 0
        dfDataMining['change_2'].iloc[i] = 0
        dfDataMining['change_3'].iloc[i] = 0
        dfDataMining['change_4'].iloc[i] = 0
        dfDataMining['change_5'].iloc[i] = 0
        dfDataMining['value_1'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_2'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_3'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_4'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_5'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_6'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_7'].iloc[i] = dfDataMining['value'].iloc[i]
        dfDataMining['value_8'].iloc[i] = dfDataMining['value'].iloc[i]
    else:
        dfDataMining['value_1'].iloc[i] = dfDataMining['value'].iloc[i-1]
        dfDataMining['value_2'].iloc[i] = dfDataMining['value_1'].iloc[i-1]
        dfDataMining['value_3'].iloc[i] = dfDataMining['value_2'].iloc[i-1]
        dfDataMining['value_4'].iloc[i] = dfDataMining['value_3'].iloc[i-1]
        dfDataMining['value_5'].iloc[i] = dfDataMining['value_4'].iloc[i-1]
        dfDataMining['value_6'].iloc[i] = dfDataMining['value_5'].iloc[i-1]
        dfDataMining['value_7'].iloc[i] = dfDataMining['value_6'].iloc[i-1]
        dfDataMining['value_8'].iloc[i] = dfDataMining['value_7'].iloc[i-1]
        dfDataMining['change_bitcoin'].iloc[i] = (dfDataMining['bitcoin'].iloc[i] * 100 / dfDataMining['bitcoin'].iloc[i-1]) - 100
        dfDataMining['change_unique'].iloc[i] = (dfDataMining['unique'].iloc[i] * 100 / dfDataMining['unique'].iloc[i-1]) - 100
        dfDataMining['change_revenue'].iloc[i] = (dfDataMining['revenue'].iloc[i] * 100 / dfDataMining['revenue'].iloc[i-1]) - 100
        dfDataMining['change_trade_volume'].iloc[i] = (dfDataMining['trade_volume'].iloc[i] * 100 / dfDataMining['trade_volume'].iloc[i-1]) - 100
        dfDataMining['change_market_cap'].iloc[i] = (dfDataMining['market_cap'].iloc[i] * 100 / dfDataMining['market_cap'].iloc[i-1]) - 100
        dfDataMining['change'].iloc[i] = (dfDataMining['value'].iloc[i] * 100 / dfDataMining['value_1'].iloc[i]) - 100
        dfDataMining['change_1'].iloc[i] = (dfDataMining['value_1'].iloc[i] * 100 / dfDataMining['value_2'].iloc[i]) - 100
        dfDataMining['change_2'].iloc[i] = (dfDataMining['value_2'].iloc[i] * 100 / dfDataMining['value_3'].iloc[i]) - 100
        dfDataMining['change_3'].iloc[i] = (dfDataMining['value_3'].iloc[i] * 100 / dfDataMining['value_4'].iloc[i]) - 100
        dfDataMining['change_4'].iloc[i] = (dfDataMining['value_4'].iloc[i] * 100 / dfDataMining['value_5'].iloc[i]) - 100
        dfDataMining['change_5'].iloc[i] = (dfDataMining['value_5'].iloc[i] * 100 / dfDataMining['value_6'].iloc[i]) - 100


    i = i + 1

print("... LAST STEP")

dfnew = classifier(dfDataMining)

dfnew.to_csv('data_mining.csv', index=False)

print("... FINISH")