import matplotlib.pyplot as plt
import streamlit as st
from fuzzy_diagnosis import inputs, disease

def plot_symptom_graphs(row):
    # Bar chart of symptom values
    plt.figure(figsize=(12,4))
    plt.bar(row.index, row.values)
    plt.xticks(rotation=45, ha='right')
    plt.ylabel("Symptom Severity")
    plt.title("Patient Symptoms")
    st.pyplot(plt)

def plot_probability_distribution(row, diagnosis_output):
    st.subheader("🔹 Fuzzy Probability Distribution")
    
    fig, ax = plt.subplots(figsize=(8,4))
    
    # Plot disease membership functions
    for label in disease.terms.keys():
        mf = disease[label].mf
        ax.plot(disease.universe, mf, label=label)
    
    # Plot predicted value
    ax.axvline(diagnosis_output, color='red', linestyle='--', label=f"Predicted: {diagnosis_output:.2f}")
    
    ax.set_title("Disease Probability Distribution")
    ax.set_xlabel("Disease Score")
    ax.set_ylabel("Membership")
    ax.legend()
    st.pyplot(fig)
