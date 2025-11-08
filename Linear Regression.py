import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    'Jumlah_Iklan' : [2, 4, 6, 8, 10],
    'Jumlah_Pembeli' : [45, 50, 65, 80, 85]
}
df = pd.DataFrame(data)

sns.scatterplot(data=df, x ='Jumlah_Iklan', y= 'Jumlah_Pembeli')
plt.title('Hubungan jumlah iklan dengan jumlah pembeli')
plt.show

X = df [['Jumlah_Iklan']]
y = df ['Jumlah_Pembeli']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Eror {mse}')

plt.scatter(X, y, color='blue')
plt.plot(X, model.predict(X), color='red')
plt.title('Linear Progression')
plt.xlabel('Jumlah Iklan')
plt.ylabel('Jumlah Pembeli')
plt.show()