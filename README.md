# ExoDetectAI

AI-enabled Detection of Exoplanets from Noisy Astronomical Light Curves

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## Overview

ExoDetectAI is an AI-powered system developed for the Bharatiya Antariksh Hackathon (BAH) 2026 organized by ISRO. The project aims to automatically detect and classify exoplanet transit signals from noisy astronomical light curves obtained from space telescopes such as TESS.

The system analyzes stellar brightness variations, identifies potential transit events, estimates important transit parameters, and visualizes the detected signals through an interactive dashboard.

## Problem Statement

### AI-enabled Detection of Exoplanets from Noisy Astronomical Light Curves

Develop an AI-based data analysis pipeline capable of automatically detecting exoplanet transit signals from noisy astronomical light curve data.

The solution should:

* Detect periodic dips in stellar brightness
* Identify potential exoplanet transit events
* Classify astrophysical signals
* Estimate transit parameters
* Provide confidence levels
* Visualize detected events

## Features

### Current Features

* Upload Light Curve CSV files
* Interactive Streamlit Dashboard
* Light Curve Visualization
* Transit Event Detection
* Transit Depth Estimation
* Confidence Score Display
* User-Friendly Interface

### Planned Features

* Real TESS Dataset Integration
* Period Detection using Astropy
* Signal-to-Noise Ratio (SNR) Calculation
* Transit Duration Estimation
* Machine Learning Classification
* Exoplanet Candidate Ranking
* Automated Report Generation

## Project Workflow

TESS Light Curves
        │
        ▼
Data Preprocessing
        │
        ▼
Noise Reduction
        │
        ▼
Transit Detection
        │
        ▼
Feature Extraction
        │
        ▼
Signal Classification
        │
        ▼
Parameter Estimation
        │
        ▼
Visualization Dashboard

## Tech Stack

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Matplotlib
* Scikit-Learn
* Lightkurve
* Astropy
* Streamlit

### Development Tools

* VS Code
* Git
* GitHub

## Folder Structure

ExoDetectAI
│
├── assets
│   ├── dashboard.png
│   ├── graph.png
│   └── prediction.png
│
├── data
│   └── sample_lightcurve.csv
│
├── dashboard
│   └── app.py
│
├── src
│
├── requirements.txt
│
├── README.md
│
└── LICENSE

## Installation

Clone the repository:

git clone https://github.com/ps0303115-cell/ExoDetectAI.git

Move into the project directory:

cd ExoDetectAI

Install dependencies:

pip install -r requirements.txt

## Running the Application

Start the Streamlit application:

streamlit run dashboard/app.py

The application will open at:

http://localhost:8501

## Sample Dataset Format

time,flux
1,1.00
2,0.99
3,1.01
4,1.00
5,0.85
6,1.00

## Sample Output

### Prediction

Potential Transit Detected

### Confidence Score

95%

### Estimated Parameters

Transit Depth : 16%
Period : 5.42 Days

## Screenshots

### Dashboard

assets/dashboard.png

### Light Curve Visualization

assets/graph.png

### Prediction Result

assets/prediction.png

## Future Scope

* Deep Learning-based Transit Detection
* Convolutional Neural Networks (CNN)
* Improved Noise Filtering
* Multi-Class Astrophysical Signal Classification
* Large Scale TESS Data Processing
* Automated Candidate Verification
* Integration with Public Astronomical Databases

## Hackathon Information

**Event:** Bharatiya Antariksh Hackathon 2026

**Organizer:** ISRO

**Problem Statement:** AI-enabled Detection of Exoplanets from Noisy Astronomical Light Curves

**Team Project:** ExoDetectAI

## License

This project is licensed under the MIT License.