import numpy as np
from arch import arch_model


def fit_garch(returns):

    model = arch_model(
        returns * 100,
        vol="GARCH",
        p=1,
        q=1
    )

    result = model.fit(
        disp="off"
    )

    return result


def forecast_volatility(
    model_result,
    horizon=20
):

    forecast = model_result.forecast(
        horizon=horizon
    )

    variance = forecast.variance.iloc[-1]

    volatility = np.sqrt(variance)

    return volatility