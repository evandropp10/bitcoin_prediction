import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing.text import one_hot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics

df = pd.read_csv('data_mining.csv')

x = df[['change_bitcoin', 'change_revenue', 'change_trade_volume', 'change_market_cap', 'change']]
y = df[['change_tomorrow']]
scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

# Para no final multiplicar o percentual de variação pelo valor e chegar ao resultado final
x_val = df[['value']]
y_val = df[['value_tomorrow']]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

x_val_train_val, x_val_test, y_val_train, y_val_test = train_test_split(x_val, y_val, test_size=0.2, random_state=101)

### Transformando em um numpy array soemente com números
x_arrTrain = np.array(x_train)
x_arrTest = np.array(x_test)
y_arrTrain = np.array(y_train)
y_arrTest = np.array(y_test)
###

### Usando Perceptron

# create model
model = Sequential()

model.add(Dense(15, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

model.compile(loss='mse', optimizer='adam')

model.fit(x_arrTrain, y_arrTrain, epochs=150, verbose=1)
print('Finish Fit')

predictions = model.predict(x_arrTest)

y_test = scale.inverse_transform(y_test)
predictions = scale.inverse_transform(predictions)

print('MAE Percentual Variação:', metrics.mean_absolute_error(y_test, predictions))

#### Transformando o percentual para valor
test_final = y_val_test
prediction_final = x_val_test + (predictions * x_val_test/ 100)
#print(prediction_final, test_final)
print('MAE Final:', metrics.mean_absolute_error(test_final, prediction_final))







