import pandas as pd
from datetime import datetime
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

df = pd.read_csv('.//data//sphist.csv',parse_dates=['Date'])
df = df.sort_values(by='Date').reset_index(drop=True)

stock = df.set_index('Date').copy()
stock = stock.resample('D').ffill()

#price indicators
stock['price_mean_5'] = stock['Close'].rolling(window=5).mean()
stock['price_mean_5']  = stock['price_mean_5'].shift(periods=1)

stock['price_adj_1'] = stock['Adj Close'].rolling(window=1).mean()
stock['price_adj_1']  = stock['price_adj_1'].shift(periods=1)

stock['price_mean_365'] = stock['Close'].rolling(window=365).mean()
stock['price_mean_365']  = stock['price_mean_365'].shift(periods=1)

#price std
stock['std_5_price'] = stock['Close'].rolling(window=5).std()
stock['std_5_price'] = stock['std_5_price'].shift(periods=1)


stock['std_365_price'] = stock['Close'].rolling(window=365).std()
stock['std_365_price'] = stock['std_365_price'].shift(periods=1)


# price ratio
stock['ratio_5_365_mean_price'] = stock['price_mean_5']/stock['price_mean_365']

stock['ratio_5_365_std_price'] = stock['std_5_price']/stock['std_365_price']

lowest_price = stock['Low'].rolling(window=365).min()
lowest_price = lowest_price.shift(periods=1)
stock['ratio_lowest_price'] = stock['Close']/lowest_price

#Volume indicator
stock['vol_mean_5'] = stock['Volume'].rolling(window=5).mean()
stock['vol_mean_5']  = stock['vol_mean_5'].shift(periods=1)

stock['vol_mean_365'] = stock['Volume'].rolling(window=365).mean()
stock['vol_mean_365']  = stock['vol_mean_365'].shift(periods=1)

#volume std
stock['std_5_vol'] = stock['Volume'].rolling(window=5).std()
stock['std_5_vol'] = stock['std_5_vol'].shift(periods=1)

stock['std_365_vol'] = stock['Volume'].rolling(window=365).std()
stock['std_365_vol'] = stock['std_365_vol'].shift(periods=1)

#volume ratio

stock['ratio_5_365_mean_vol'] = stock['vol_mean_5']/stock['vol_mean_365']

stock['ratio_5_365_std_vol'] = stock['std_5_vol']/stock['std_365_vol']

#stock.iloc[:,6:] = (stock.iloc[:,6:] - stock.iloc[:,6:].min())/ (stock.iloc[:,6:].max() - stock.iloc[:,6:].min())
# data split
stock = stock.dropna()
train = stock[stock.index < datetime(2013,1,1)].copy()
test = stock[stock.index >= datetime(2013,1,1)].copy()
#test = test.iloc[:100]

#model 
features = ['price_mean_5','price_adj_1','vol_mean_5','price_mean_365','ratio_5_365_std_vol']
target = 'Close'
lr = LinearRegression()
lr.fit(train[features],train[target])
predictions = lr.predict(test[features])

# Accuracy calculations
mse = mean_absolute_error(test[target],predictions)
test['pred'] = predictions


#print(test[['Close','pred']].head(10))                       
print(stock[stock.index > datetime(1951,1,2)].head())
print(mse)

plt.figure(figsize=(18,12))
plt.xlabel('Date',fontsize=10)
plt.plot(train['Close'])
plt.plot(test['pred'],c='orange',linewidth=0.2)
plt.plot(test['Close'],c='red',linewidth=0.2)
plt.show()
# TODO: add data on New york city weather and twitter activity
# TODO: add days off in prev month
# TODO: make the system real-time by writing an automated script to download the latest data when the market closes, and make predictions for the next day.

