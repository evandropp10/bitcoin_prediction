import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import KFold
from sklearn import metrics
from sklearn.preprocessing import MinMaxScaler

df = pd.read_csv('data_mining.csv')

#x = df[['bitcoin','bitcoin buy','bitcoin mining', 'bitcoin price', 'blockchain']]
x = df[['bitcoin', 'revenue', 'trade_volume', 'market_cap', 'value']]
y = df[['value_tomorrow']]
scale = MinMaxScaler()
x = scale.fit_transform(x)
y = scale.fit_transform(y)


xnp = np.array(x)
ynp = np.array(y)

### Usando Perceptron

# create model
model = Sequential()
model.add(Dense(15, input_dim=5, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='linear'))

# Compile model
model.compile(loss='mse', optimizer='adam')

result_final = pd.DataFrame(columns=['test', 'prediction'])

## Cross Validation
kFold = KFold(n_splits=6)

for train_index, test_index in kFold.split(xnp):
    
    x_train, x_test = xnp[train_index], xnp[test_index]
    y_train, y_test = ynp[train_index], ynp[test_index]

    model.fit(x_train, y_train, epochs=150, verbose=0)

    predictions = model.predict(x_test)

    result = pd.DataFrame(columns=['test', 'prediction'])

    y_test_ok = np.reshape(y_test[:,0], (-1,1))
    
    result_test = scale.inverse_transform(y_test_ok)
    result_prediction = scale.inverse_transform(predictions)
   
    result['test'] = result_test.reshape((-1,1))[:,0]
    result['prediction'] = result_prediction.reshape((-1,1))

    print(result)
    result_final = pd.concat([result_final, result])

    print('MAE:', metrics.mean_absolute_error(result['test'], result['prediction']))

print('MAE Final:', metrics.mean_absolute_error(result_final['test'], result_final['prediction']))



