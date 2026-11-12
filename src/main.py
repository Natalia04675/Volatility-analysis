import yfinance as yf
import numpy as np

from src.historical_volatility import compute_historical_vol

from src.volatility_smile import (
    build_volatility_smile,
    plot_smile
)

from src.garch_model import (
    fit_garch,
    forecast_volatility
)

from src.volatility_risk import (
    compute_vrp
)

from src.volatility_comparison import (
    compare_models
)


def main():

    print("=" * 50)
    print("SP500 VOLATILITY ANALYTICS PLATFORM")
    print("=" * 50)

    # ------------------------------------------------
    # DATA
    # ------------------------------------------------

    spy = yf.download(
    "SPY",
    period="5y",
    auto_adjust=True
)
    if spy.empty:
     
     raise ValueError(
        "SPY download failed"
    )

    returns = np.log(
        spy["Close"] /
        spy["Close"].shift(1)
    )

    returns = returns.dropna()

  

    historical_vol = float(
        returns.std()
        * np.sqrt(252)
    )

    print()
    print(f"Historical Volatility: {historical_vol:.2%}")



    smile_df = build_volatility_smile()

    plot_smile(smile_df)

    atm_iv = smile_df.iloc[
        (smile_df["Strike"] -
         smile_df["Strike"].median()
        ).abs().argsort()[:1]
    ]["IV"].values[0]

    print(
        f"ATM Implied Volatility: {atm_iv:.2%}"
    )



    garch_model = fit_garch(returns)

    garch_forecast = (
        forecast_volatility(
            garch_model
        )
    )

    print(
        f"GARCH Forecast: {garch_forecast.iloc[0]:.2f}%"
    )


    vrp = compute_vrp(
        atm_iv,
        historical_vol
    )

    print(
        f"Volatility Risk Premium: {vrp:.2%}"
    )

 
    

    comparison = compare_models(
        historical_vol,
        atm_iv,
        garch_forecast.iloc[0] / 100
    )

    print()
    print(comparison)


if __name__ == "__main__":
    main()
