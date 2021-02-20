import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from datetime import datetime
from matplotlib.pyplot import figure

df = pd.read_csv("asics-gel-lyte-iii-atmos-x-solebox.csv")
df["Sale Date"] = pd.to_datetime(df["Sale Date"])
df.index = df["Sale Date"]

print(df.info())
print(df.head())

size_7 = df[df["Size"] == 7]
size_8 = df[df["Size"] == 8]

size_7_plot_days = size_7.groupby(pd.Grouper(freq='D')).mean()
size_7_plot_5days = size_7.groupby(pd.Grouper(freq='7D')).mean()
size_7_plot_month = size_7.groupby(pd.Grouper(freq='M')).mean()
size_8_plot = size_8.groupby(pd.Grouper(freq='D')).mean()
size_8_plot_5days = size_8.groupby(pd.Grouper(freq='7D')).mean()

# plt.plot(size_8_plot.index, size_8_plot["Sale Price"])
# plt.xticks(rotation=90)
# plt.savefig('size_8_sales.png')

# fig, axs = plt.subplots(1, 3, figsize=(20, 10), sharey=True)
# plt.xticks(rotation=90)
# plt.setp(axs[0].xaxis.get_majorticklabels(),rotation = 90)
# plt.setp(axs[1].xaxis.get_majorticklabels(),rotation = 90)
# plt.setp(axs[2].xaxis.get_majorticklabels(),rotation = 90)
# axs[0].plot(size_7_plot_days.index, size_7_plot_days["Sale Price"])
# axs[1].plot(size_7_plot_5days.index, size_7_plot_5days["Sale Price"])
# axs[2].plot(size_7_plot_month.index, size_7_plot_month["Sale Price"])


# fig = figure(figsize=(10,10))
# plt.plot(size_7_plot_5days.index, size_7_plot_5days["Sale Price"])
# plt.setp(axs[0].xaxis.get_majorticklabels(),rotation = 90)
# plt.setp(axs[1].xaxis.get_majorticklabels(),rotation = 90)

fig, axs = plt.subplots(1, 2, figsize=(20, 10), sharey=True)
axs[0].plot(size_8_plot_5days.index, size_8_plot_5days["Sale Price"])
axs[1].plot(size_7_plot_5days.index, size_7_plot_5days["Sale Price"])
plt.xlabel("Sale Date")
plt.ylabel("Sale Price")
fig.savefig('size_7_sales.png')

# fig1 = plt.figure(figsize=(10, 10))
# plt.plot(size_8_plot.index, size_8_plot["Sale Price"])
# plt.xticks(rotation=90)
# plt.savefig('size_8_sales.png')

