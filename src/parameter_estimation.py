import numpy as np

def estimate_parameters(flux):
    depth = 1 - np.min(flux)

    return {
        "transit_depth": round(float(depth), 5)
    }