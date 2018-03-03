import pandas as pd

from yahoo_historical import Fetcher

df = pd.read_csv('ind_nifty50list.csv', parse_dates=True, index_col=0)

-- print(df)

data = Fetcher("AAPL", [2007,1,1], [2017,1,1])
data = Fetcher()
print(data.getHistorical())