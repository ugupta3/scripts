import logging
import  KiteClient as kite

logging.basicConfig(level=logging.DEBUG)

kite.place_order(tradingsymbol="SBIN",transaction_type="BUY",quantity=1,price=261)