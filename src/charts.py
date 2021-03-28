import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt
import datetime as dt
from matplotlib.pyplot import figure
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, LSTM

#Prepare data

start = dt.datetime(2020,12,1)
end = dt.datetime(2021,3,1)

df = pd.read_csv("../assets/data/air-jordan-1-mid-banned-2020.csv")
df["Sale Date"] = pd.to_datetime(df["Sale Date"])
df.index = df["Sale Date"]
df = df[df["Size"]==7]
df["Sale Price"] = df["Sale Price"].groupby(pd.Grouper(freq='1D')).mean()
df = df.dropna()

data = df[df["Sale Date"] < "2021-02-24"]

scaler = MinMaxScaler(feature_range=(0,1))
scaled_data = scaler.fit_transform(data["Sale Price"].values.reshape(-1,1))

prediction_days = 60

x_train = []
y_train = []

for x in range(prediction_days, len(scaled_data)):
    x_train.append(scaled_data[x-prediction_days:x,0])
    y_train.append(scaled_data[x,0])

x_train, y_train = np.array(x_train), np.array(y_train)

x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

# Build the model

model = Sequential()

model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=50))
model.add(Dropout(0.2))
model.add(Dense(units=1)) # prediction of the next price

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(x_train, y_train, epochs=20, batch_size=50)

# Test the model accuracy on existing data

test_start = dt.datetime(2020,2,24)
test_end = dt.datetime.now()

test_data = df[df["Sale Date"]>"2021-02-24"]
actual_prices = test_data["Sale Price"].values

total_dataset = pd.concat((data["Sale Price"], test_data["Sale Price"]), axis = 0)

model_inputs = total_dataset[len(total_dataset) - len(test_data) - prediction_days:].values
model_inputs = model_inputs.reshape(-1,1)
model_inputs = scaler.transform(model_inputs)

print(model_inputs)

# Make predictions on test data

x_test = []

for x in range(prediction_days, len(model_inputs)):
    x_test.append(model_inputs[x-prediction_days:x,0])

x_test = np.array(x_test)
x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

prediction_prices = model.predict(x_test)
prediction_prices = scaler.inverse_transform(prediction_prices)

plt.plot(actual_prices, color="black", label="Actual price")
plt.plot(prediction_prices, color="green",label="Predicted price")
plt.xlabel("Time")
plt.ylabel("Price")
plt.legend()
plt.show()

#print(df.info())
#print(df.head())







""" size_7 = df[df["Size"] == 7]
size_8 = df[df["Size"] == 8]

size_7_plot_days = size_7.groupby(pd.Grouper(freq='D')).mean()
size_7_plot_5days = size_7.groupby(pd.Grouper(freq='5D')).mean()
size_7_plot_month = size_7.groupby(pd.Grouper(freq='M')).mean()
size_8_plot = size_8.groupby(pd.Grouper(freq='D')).mean()
size_8_plot_5days = size_8.groupby(pd.Grouper(freq='5D')).mean()


fig, axs = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
axs[0].plot(size_8_plot_5days.index, size_8_plot_5days["Sale Price"])
axs[1].plot(size_7_plot_5days.index, size_7_plot_5days["Sale Price"])
plt.xlabel("Sale Date")
plt.ylabel("Sale Price")
fig.savefig('size_7_sales.png')
 """
