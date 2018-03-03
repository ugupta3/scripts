import urllib.request, json
from matplotlib import style
import pandas as pd
import schedule
import time
import datetime
from pandas.io.json import json_normalize

style.use('ggplot')


def getStockPrice(tick):
    urlTick = "https://query2.finance.yahoo.com/v7/finance/quote?symbols=" + tick + ".NS"
    #print(urlTick)
    return json.loads(urllib.request.urlopen(urlTick).read().decode());



def generateSignal(tick):
    stockPrice = getStockPrice(tick)

    df = json_normalize(stockPrice['quoteResponse']['result'][0])
    current_price = df['regularMarketPrice'].at[0];
    regular_market_open = df['regularMarketOpen'].at[0]
    fifty_day_average = df['fiftyDayAverage'].at[0]
    two_hundred_day_average = df['twoHundredDayAverage'].at[0]
   # print("current_price s", current_price)

    if fifty_day_average > two_hundred_day_average and fifty_day_average-two_hundred_day_average<=1:
        print("Buy stock " + tick)


nfty50 = pd.read_csv('ind_nifty50list.csv', parse_dates=True, index_col=0)["Symbol"]


def mainTask():
    for x in range(len(nfty50.index)):
        generateSignal(nfty50.iloc[x])


schedule.every(1).seconds.do(mainTask)

while True:
    schedule.run_pending()

    print("Done with processing @" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") )
    time.sleep(5)
