import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['bitcoin', 'revenue', 'trade_volume', 'market_cap', 'value']]
y = df[['value_tomorrow']]
scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

lr = LinearRegression()

lr.fit(x_train, y_train)

prediction = lr.predict(x_test)
prediction
y_test = scale.inverse_transform(y_test)
prediction = scale.inverse_transform(prediction)

###-----

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, prediction))

#result.to_csv('result_linearRegression-03.csv')
