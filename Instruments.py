import pandas as pd


class InstrumentsProvider:

    def __init__(self):
        self.df = pd.read_csv('instruments.csv')
        self.nse = self.df[(self.df['exchange'] == "NSE") & (self.df['instrument_type'] == "EQ")].set_index(
            "tradingsymbol")
        self.bse = self.df[(self.df['exchange'] == "BSE") & (self.df['instrument_type'] == "EQ")].set_index(
            "tradingsymbol")

    def get_instrument_token(self, tradingsymbol, exchange="NSE"):
        if (exchange == "NSE"):
            return self.nse.loc[tradingsymbol, "instrument_token"].astype(str)
        else:
            return self.bse.loc[tradingsymbol, "instrument_token"].astype(str)




