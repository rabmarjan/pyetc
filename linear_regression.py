import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

income = [[2000], [2500], [2700], [3900], [4100], [4550]]
expenditure = [1950, 2400, 2500, 3800, 3950, 4410]

X = np.array(income)
Y = np.array(expenditure)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=1)
model = LinearRegression()
model.fit(X_train, Y_train)
print("The intercept of the model: {}".format(model.intercept_))
print("Coefficient of variable: {}".format(model.coef_))

# The sum squared error
print("Sum of squared error: {}".format(np.sum(model.predict(X_test) - Y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: {}'.format(model.score(X_test, Y_test)))
