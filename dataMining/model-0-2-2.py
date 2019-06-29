import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['bitcoin', 'revenue', 'trade_volume', 'market_cap', 'value']]
y = df[['value_tomorrow']]

scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

pf = PolynomialFeatures(degree=2)
x_poly = pf.fit_transform(x)

lr = LinearRegression()

prediction = cross_val_predict(lr, x_poly, y, cv=22)

y_test = scale.inverse_transform(y)
prediction = scale.inverse_transform(prediction)

#result = pd.DataFrame(columns=['Date', 'Test', 'Prediction'])
#
#result['Date'] = df['date']
#result['Test'] = y['value_tomorrow']
#result['Prediction'] = prediction


###-----


print('MAE:', metrics.mean_absolute_error(y_test,prediction))





