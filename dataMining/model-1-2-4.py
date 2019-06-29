import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_predict
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['change_bitcoin', 'change_revenue', 'change_trade_volume', 'change_market_cap', 'change']]
y = df[['change_tomorrow']]

# Para no final multiplicar o percentual de variação pelo valor e chegar ao resultado final
x_val = df[['value']]
y_val = df[['value_tomorrow']]

scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

model = GradientBoostingRegressor(loss='lad', max_depth=10,
                                max_features=None,
                                min_samples_leaf=6,
                                min_samples_split=6,
                                n_estimators=500)

prediction = cross_val_predict(model, x, y, cv=20)

y = np.reshape(y, (-1,1))
y_test = scale.inverse_transform(y)
prediction = np.reshape(prediction, (-1,1))
prediction = scale.inverse_transform(prediction)

print('MAE Percentual Variação:', metrics.mean_absolute_error(y_test, prediction))

#### Transformando o percentual para valor
test_final = y_val
prediction_final = x_val + (prediction * x_val/ 100)
#print(prediction_final, test_final)
print('MAE Final:', metrics.mean_absolute_error(test_final, prediction_final))

