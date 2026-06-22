import numpy as np
from astropy.timeseries import BoxLeastSquares

def detect_transit(time, flux):
    model = BoxLeastSquares(time, flux)
    periods = np.linspace(0.5, 10, 1000)
    result = model.power(periods, 0.2)
    best_period = result.period[np.argmax(result.power)]

    return {
        "period": float(best_period), "power": float(np.max(result.power))
    }