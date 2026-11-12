import pandas as pd


def compare_models(
    historical_vol,
    implied_vol,
    garch_vol
):

    comparison = pd.DataFrame({
        "Metric": [
            "Historical Volatility",
            "Implied Volatility",
            "GARCH Forecast"
        ],
        "Value": [
            historical_vol,
            implied_vol,
            garch_vol
        ]
    })

    print(comparison)

    return comparison