

import numpy as np


def compute_historical_vol(
    returns
):

    return (
        returns.std()
        * np.sqrt(252)
    )
