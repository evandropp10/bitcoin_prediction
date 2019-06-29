import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_predict
from sklearn import metrics

dfData = pd.read_csv('data-mining.csv')

x = dfData[['bitcoin', 'change', 'change1', 'change2', 'change3', 'change4', 'change5', 'unique']]
y = dfData[['classChangeTomorrow']]

gnb = GaussianNB()

prediction = cross_val_predict(gnb, x, y, cv=10)

result = pd.DataFrame(columns=['Test', 'Prediction'])

result = pd.DataFrame(columns=['Date', 'Test', 'Prediction'])

result['Date'] = dfData['date']
result['Test'] = y['classChangeTomorrow']
result['Prediction'] = prediction


print('Accuracy:', metrics.accuracy_score(result['Test'],result['Prediction']))