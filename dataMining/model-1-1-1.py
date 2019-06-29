import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
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

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

x_val_train_val, x_val_test, y_val_train, y_val_test = train_test_split(x_val, y_val, test_size=0.2, random_state=101)


lr = LinearRegression()

lr.fit(x_train, y_train)

prediction = lr.predict(x_test)
prediction
y_test = scale.inverse_transform(y_test)
prediction = scale.inverse_transform(prediction)

print('MAE Percentual Variação:', metrics.mean_absolute_error(y_test, prediction))

#### Transformando o percentual para valor
test_final = y_val_test
prediction_final = x_val_test + (prediction * x_val_test/ 100)
#print(prediction_final, test_final)
print('MAE Final:', metrics.mean_absolute_error(test_final, prediction_final))

