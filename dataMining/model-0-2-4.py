import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import cross_val_predict


df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['bitcoin', 'revenue', 'trade_volume', 'market_cap', 'value']]
y = df[['value_tomorrow']]

scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

model = GradientBoostingRegressor(loss='lad', max_depth=10,
                                max_features=None,
                                min_samples_leaf=6,
                                min_samples_split=6,
                                n_estimators=500)

prediction = cross_val_predict(model, x, y, cv=15)

y = np.reshape(y, (-1,1))
y_test = scale.inverse_transform(y)
prediction = np.reshape(prediction, (-1,1))
prediction = scale.inverse_transform(prediction)


###-----

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test,prediction))
print(y_test)
