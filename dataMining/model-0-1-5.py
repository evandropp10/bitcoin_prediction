import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler



df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['bitcoin', 'blockchain', 'revenue', 'trade_volume', 'market_cap', 'value']]
y = df[['value_tomorrow']]

scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

model = RandomForestRegressor(max_depth=10, random_state=0, n_estimators=200)

model.fit(x_train, y_train)
print('Finish Fit')
prediction = model.predict(x_test)

predictions = np.reshape(prediction, (-1,1))
predictions
y_test
y_test = scale.inverse_transform(y_test)
prediction = scale.inverse_transform(predictions)

###-----

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, prediction))
