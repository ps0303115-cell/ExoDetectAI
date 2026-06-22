def classify_signal(depth):

    if depth < 0.03:
        return "Possible Exoplanet"

    elif depth < 0.15:
        return "Eclipsing Binary"

    return "Noise/Other"