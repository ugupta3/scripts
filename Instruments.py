import pandas as pd


class Instruments:

    def __init__(self):
        self.df = pd.read_csv('instruments.csv', parse_dates=True, index_col=0)
        self.nse = self.df[(self.df['exchange'] == "NSE") & (self.df['instrument_type'] == "EQ")].set_index(
            "tradingsymbol")
        self.bse = self.df[(self.df['exchange'] == "BSE") & (self.df['instrument_type'] == "EQ")].set_index(
            "tradingsymbol")

    def get_instrument_token(self, tradingsymbol="SBIN", exchange="NSE"):
        if (exchange == "NSE"):
            return self.nse.loc[tradingsymbol, "exchange_token"]
        else:
            return self.bse.loc[tradingsymbol, "exchange_token"]


instruments = Instruments()

print(instruments.get_instrument_token())


