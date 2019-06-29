import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.preprocessing.text import one_hot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data_mining.csv')

x = df[['bitcoin', 'revenue', 'market_cap', 'trade_volume', 'value']]
y = df[['value_tomorrow']]
scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

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

model.fit(x_arrTrain, y_arrTrain, epochs=700, verbose=1)
print('Finish Fit')
x_arrTest
predictions = model.predict(x_arrTest)

from sklearn import metrics
y_test = scale.inverse_transform(y_test)
predictions = scale.inverse_transform(predictions)
print('MAE:', metrics.mean_absolute_error(y_test,predictions))


result.to_csv('result_perceptron-01.csv')

