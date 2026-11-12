
import yfinance as yf


def get_spy_data():

    spy = yf.download(
        "SPY",
        period="5y",
        auto_adjust=True
    )

    if spy.empty:
        raise ValueError(
            "SPY data download failed"
        )

    return spy