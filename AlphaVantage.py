from alpha_vantage.timeseries import TimeSeries

from pprint import pprint

ts = TimeSeries(key='5R7DFAFNKLGBJ1Z7',output_format='pandas')



data, meta_data = ts.get_monthly(symbol='YESBANK')
pprint(data.head(2))