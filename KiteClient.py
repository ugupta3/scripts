import requests
import json
import urllib

KITE_HOST = 'https://kite3.zerodha.com/api/'

KITE_CHART_API_HOST='https://kitecharts.zerodha.com/api/chart/'

ORDERS_API = KITE_HOST + "orders"

headers = {"Cookie": "kfsession=Zz34Hooj7yK0nn8HIm3kVPheYTT5XJjp",
           "X-CSRFToken": "c9cc6bbd65f59e8c6e31c1d376858a9f",
           "Origin": "https://kite3.zerodha.com"
           }


def holdings():
    url = KITE_HOST + 'portfolio/holdings'
    headers
    r = requests.get(url, headers=headers)
    print(r.json())


def orders():
    r = requests.get(ORDERS_API, headers=headers)
    print(r.json())


def positions():
    url = KITE_HOST + 'portfolio/positions'
    headers
    r = requests.get(url, headers=headers)
    print(r.json())


def place_order(tradingsymbol,
                transaction_type,
                quantity,
                price,
                order_type="LIMIT",
                product="MIS",
                exchange="NSE",
                validity="DAY",
                disclosed_quantity="0",
                trigger_price="0",
                squareoff="0",
                stoploss="0",
                trailing_stoploss="0",
                variety="regular",
                client_id="PS9155"):
    payload = locals();
    print(payload)
    r = requests.session().post(ORDERS_API+"/"+variety, headers=headers, data=payload)
    print(r.json())


def getHistory():
    return

#holdings()
#orders()
#positions()
place_order("SBIN","BUY","1","261")
