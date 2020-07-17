import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn import datasets, linear_model
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
from sklearn.model_selection import cross_val_predict




# Load Data From CSV
data_raw = pd.read_csv('/Users/tongjia/Desktop/CCBGJJ/ccbML/x_jce_0827.csv')
data_raw.count()

data_raw.shape

data_raw.head()


# Check every relationship between every X and y
d1 = data_raw.copy()
plt.subplot()
plt.scatter(d1['spgz'], d1['jce'])
plt.show()

plt.scatter(d1['sjrs'], d1['jce'])
plt.show()

plt.scatter(d1['xhrs'], d1['jce'])
plt.show()

plt.scatter(d1['xzkhs'], d1['jce'])
plt.show()

d = d1


# filter data and check again if necessary
d = data_raw[data_raw['jce'] < 2000000000].copy()
plt.subplot()
plt.scatter(d['spgz'], d['jce'])
plt.show()

plt.scatter(d['sjrs'], d['jce'])
plt.show()

plt.scatter(d['xhrs'], d['jce'])
plt.show()

plt.scatter(d['xzkhs'], d['jce'])
plt.show()


# Define X y in Model
X = d[['spgz','sjrs','xhrs','xzkhs']]
y = d[['jce']]


# Define Train Model
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# Fit model
linreg = LinearRegression()
linreg.fit(X_train, y_train)


# Check score
linreg.score(X_test, y_test)


# Check MSE/RMSE
y_pred = linreg.predict(X_test)


# scikit-learn - MSE
print("MSE:", metrics.mean_squared_error(y_test, y_pred))


# scikit-learn - RMSE
print("RMSE:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))


# cross_val_predict
predicted = cross_val_predict(linreg, X, y, cv=10)


# scikit-learn - MSE
print("MSE:", metrics.mean_squared_error(y, predicted))


# scikit-learn - RMSE
print("RMSE:", np.sqrt(metrics.mean_squared_error(y, predicted)))


# Check result - polt
fig, ax = plt.subplots()
ax.scatter(y, predicted)
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()