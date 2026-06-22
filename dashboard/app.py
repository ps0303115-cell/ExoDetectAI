import streamlit as st
from lightkurve import search_lightcurve
import matplotlib.pyplot as plt

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.preprocessing import clean_lightcurve
from src.transit_detection import detect_transit
from src.parameter_estimation import estimate_parameters
from src.classifier import classify_signal

st.title("ExoDetectAI")
st.write("AI Enabled Exoplanet Detection System")

tic_id = st.text_input("Enter TIC ID", "25155310")

if st.button("Analyze"):
    try:
        lc = search_lightcurve(f"TIC {tic_id}", mission="TESS").download()

        lc = clean_lightcurve(lc)

        st.subheader("Light Curve")

        fig, ax = plt.subplots(figsize=(10, 4))

        ax.plot(lc.time.value, lc.flux.value, ".", markersize=1)

        ax.set_title("TESS Light Curve")
        ax.set_xlabel("Time (Days)")
        ax.set_ylabel("Flux")

        st.pyplot(fig)

        time = lc.time.value
        flux = lc.flux.value

        transit = detect_transit(time, flux)

        params = estimate_parameters(flux)

        prediction = classify_signal(params["transit_depth"])

        st.subheader("Results")

        st.write(f"Detected Period: {transit['period']:.2f} days")

        st.write(f"Transit Depth: {params['transit_depth']:.5f}")

        if prediction == "Possible Exoplanet":
            st.success(f"Classification: {prediction}")
        else:
            st.error(f"Classification: {prediction}")

        report = f"""ExoDetectAI Report
        TIC ID: {tic_id}
        Detected Period: {transit['period']:.2f} days
        Transit Depth: {params['transit_depth']:.5f}
        Classification: {prediction}"""

        st.download_button(label="Download Report", data=report, file_name=f"TIC_{tic_id}_report.txt", mime="text/plain")

    except Exception as e:
        st.error(f"Error: {str(e)}")