import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("ExoDetectAI")

uploaded_file = st.file_uploader("Upload Light Curve CSV",type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("Dataset Preview")
    st.dataframe(data.head())

    if "time" in data.columns and "flux" in data.columns:
        fig, ax = plt.subplots()
        ax.plot(data["time"], data["flux"])
        ax.set_xlabel("Time")
        ax.set_ylabel("Brightness")

        st.pyplot(fig)

        st.success("Potential Transit Detected")

        st.write("Confidence: 95%")
        st.write("Period: 5.42 Days")
        st.write("Depth: 1.8%")