import streamlit as st
import pandas as pd
from fuzzy_diagnosis import run_fuzzy_diagnosis
from visualize import plot_symptom_graphs, plot_probability_distribution
from ml_hybrid import run_ml_prediction

st.set_page_config(page_title="Fuzzy Disease Diagnosis", layout="wide")

st.title("🩺 Fuzzy-Based Disease Diagnosis System")

# Input selection
input_option = st.radio("Select Input Method:", ["CSV Upload", "Manual Input"])

# Initialize dataframe
user_data = None

if input_option == "CSV Upload":
    uploaded_file = st.file_uploader("Upload CSV file with patient symptoms", type="csv")
    if uploaded_file is not None:
        user_data = pd.read_csv(uploaded_file)
        st.success("✅ CSV Loaded")
        st.dataframe(user_data)

if input_option == "Manual Input":
    # Sliders for symptoms
    symptom_names = [
        'fever', 'cough', 'fatigue', 'sore_throat', 'breathing', 'nausea',
        'vomiting', 'diarrhea', 'chills', 'rash', 'smell_loss', 'chest_pain',
        'nasal_congestion', 'sweats', 'weight_loss', 'lymph_nodes', 'headache', 'body_pain'
    ]
    user_input = {}
    for sym in symptom_names:
        user_input[sym] = st.slider(sym.replace("_"," ").title(), 0, 10, 0)
    user_data = pd.DataFrame([user_input])

# Toggle sections
st.markdown("---")
show_fuzzy = st.checkbox("Show Fuzzy Diagnosis & Graphs", value=True)
show_ml = st.checkbox("Show ML Risk Prediction", value=False)

if user_data is not None:
    if show_fuzzy:
        st.header("🧠 Fuzzy Diagnosis Results")
        fuzzy_results = run_fuzzy_diagnosis(user_data)
        st.dataframe(fuzzy_results)
        # Plot graphs and probability distributions
        for idx, row in user_data.iterrows():
            st.subheader(f"Patient {idx+1} Symptom Graphs")
            plot_symptom_graphs(row)
            plot_probability_distribution(row, fuzzy_results.loc[idx, 'Fuzzy Disease Score'])

    if show_ml:
        st.header("📊 ML-Based Risk Prediction")
        ml_results = run_ml_prediction(user_data)
        st.dataframe(ml_results)
