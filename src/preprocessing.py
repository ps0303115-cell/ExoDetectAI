import numpy as np

def clean_lightcurve(lightcurve):
    lc = lightcurve.remove_outliers()
    lc = lc.normalize()

    return lc

def get_flux_statistics(lightcurve):
    flux = lightcurve.flux.value

    return {
        "mean_flux": np.mean(flux), "std_flux": np.std(flux), "min_flux": np.min(flux), "max_flux": np.max(flux)
    }