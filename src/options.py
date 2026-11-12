
import yfinance as yf


def get_option_chain():

    ticker = yf.Ticker("SPY")

    expiry = ticker.options[0]

    chain = ticker.option_chain(expiry)

    return chain.calls
