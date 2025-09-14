# Fuzzy-Based Disease Diagnosis System

## Overview

This project implements a **Fuzzy-Based Disease Diagnosis System** using Python and Streamlit. The system allows users to input patient symptoms via sliders or CSV files, performs fuzzy logic-based disease probability computation, and optionally displays machine learning-based risk predictions. The system is fully offline, interactive, and provides visualizations for symptom severity and probability distributions.

---

## Features

- Input via **CSV upload** or **manual sliders** for 18 symptoms.
- **Fuzzy Logic Diagnosis**:
  - Uses fuzzy membership functions and rules to estimate disease probability.
  - Displays patient-specific **probability distribution graphs**.
- **ML-Based Risk Prediction** (placeholder hybrid model).
- Interactive **Streamlit dashboard** with toggles for fuzzy graphs and ML predictions.
- Fully offline; no cloud services required.

---

## Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/USERNAME/REPO_NAME.git
cd REPO_NAME
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the application**

```bash
streamlit run app.py
```

5. Open the provided URL in your browser (usually `http://localhost:8501`).

---

## Usage

1. Choose **input method**: CSV or Manual sliders.
2. If CSV is selected, upload a CSV file with symptom values.
3. Toggle **Fuzzy Diagnosis & Graphs** and/or **ML Risk Prediction**.
4. View results in tables and graphs.
5. For each patient, the system displays:
   - Bar chart of symptoms.
   - Fuzzy probability distribution with predicted disease score.

---

## File Structure

```
app.py                 # Main Streamlit application
fuzzy_diagnosis.py     # Fuzzy logic computation module
visualize.py           # Visualization functions (symptom & probability graphs)
ml_hybrid.py           # ML risk prediction module (placeholder)
disease_symptoms_dataset.csv  # Sample dataset
requirements.txt       # Python dependencies
```

---

## Future Enhancements

- Integrate **real machine learning models** trained on larger datasets.
- Add **dynamic rule generation** for fuzzy logic based on dataset statistics.
- Include **disease-specific recommendations** or alerts.
- Expand dataset to cover more symptoms and diseases.
- Implement **user authentication** for multi-user dashboards.
- Enable **export of results** to CSV or PDF.
- Add **time-series tracking** for patients to monitor symptom progression.
- Enhance UI with **interactive graphs** (Plotly or Bokeh).

---

## License

This project is open-source and free to use under the MIT License.

---

## Contact

For questions or contributions, contact **Dhanakudharam Sahithi** at **sahithidhanakudharam25@gmail.com**.

