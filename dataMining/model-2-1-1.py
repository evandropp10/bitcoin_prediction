import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics


def fact_class_change(x):
    if x == "down4":
        return 1
    if x == "down3":
        return 2
    if x == "down2":
        return 3
    if x == "down1":
        return 4
    if x == "up1":
        return 5
    if x == "up2":
        return 6
    if x == "up3":
        return 7
    if x == "up4":
        return 8
    
df = pd.read_csv('data_mining.csv')

df['fact_class_change_tomorrow'] = df['class_change_tomorrow'].apply(fact_class_change)
df['fact_class_change'] = df['class_change'].apply(fact_class_change)

x = df[['change_bitcoin', 'change', 'fact_class_change', 'change_revenue']]
y = df[['fact_class_change_tomorrow']]

gnb = GaussianNB()

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=101)

gnb.fit(x_train, y_train)

prediction = gnb.predict(x_test)

result = pd.DataFrame(columns=['Test', 'Prediction'])

result['Test'] = y_test['fact_class_change_tomorrow']
result['Prediction'] = prediction

result.to_csv('gaussian_classification.csv')

print('Accuracy:', metrics.accuracy_score(result['Test'],result['Prediction']))
print(metrics.confusion_matrix(result['Test'],result['Prediction']))