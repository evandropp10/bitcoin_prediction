import pandas as pd
import seaborn as sns

dfData = pd.read_csv('data-mining.csv')
dfTest = dfData[['bitcoin', 'change', 'change1', 'change2', 'change3', 'change4', 'change5', 'unique', 'classChangeTomorrow']]

#HIT MAP
sns.pairplot(dfTest,hue='classChangeTomorrow')

#BAR PLOT
sns.barplot(x='classChangeTomorrow', y='valueTomorrow', data=dfData)

# VALUE COUNT
sns.countplot(dfTest['classChangeTomorrow'],label="Count")

###
dfTest = dfData[['changeBitcoin', 'changeTomorrow', 'changeUnique']]

#HIT MAP
sns.pairplot(dfTest,hue='changeTomorrow')

#BAR PLOT
sns.barplot(x='changeTomorrow', y='changeBitcoin', data=dfTest)