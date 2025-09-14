import pandas as pd
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define symptoms
symptom_names = [
    'fever', 'cough', 'fatigue', 'sore_throat', 'breathing', 'nausea',
    'vomiting', 'diarrhea', 'chills', 'rash', 'smell_loss', 'chest_pain',
    'nasal_congestion', 'sweats', 'weight_loss', 'lymph_nodes', 'headache', 'body_pain'
]

# Fuzzy Inputs
inputs = {name: ctrl.Antecedent(np.arange(0, 11, 1), name) for name in symptom_names}
for inp in inputs.values():
    inp['low'] = fuzz.trimf(inp.universe, [0, 0, 5])
    inp['medium'] = fuzz.trimf(inp.universe, [0, 5, 10])
    inp['high'] = fuzz.trimf(inp.universe, [5, 10, 10])

# Fuzzy Output
disease = ctrl.Consequent(np.arange(0, 11, 1), 'disease')
disease.automf(names=['low','medium','high'])

# Sample Rules
rules = [
    ctrl.Rule(inputs['fever']['high'] & inputs['cough']['high'], disease['high']),
    ctrl.Rule(inputs['rash']['high'] & inputs['fever']['medium'], disease['medium']),
    ctrl.Rule(inputs['nausea']['medium'] & inputs['vomiting']['high'], disease['high']),
    ctrl.Rule(inputs['fatigue']['high'] & inputs['body_pain']['high'], disease['high']),
    ctrl.Rule(inputs['diarrhea']['medium'] & inputs['sweats']['medium'], disease['medium']),
    ctrl.Rule(inputs['smell_loss']['high'] & inputs['nasal_congestion']['high'], disease['high']),
    ctrl.Rule(inputs['weight_loss']['high'] & inputs['lymph_nodes']['high'], disease['high']),
    ctrl.Rule(inputs['headache']['high'] & inputs['chills']['high'], disease['high']),
    ctrl.Rule(inputs['chest_pain']['medium'] & inputs['breathing']['high'], disease['high']),
    ctrl.Rule(inputs['sore_throat']['medium'] & inputs['cough']['medium'], disease['medium']),
    ctrl.Rule(inputs['smell_loss']['low'] & inputs['fever']['low'], disease['low']),
    ctrl.Rule(inputs['rash']['low'] & inputs['body_pain']['low'], disease['low'])
]

diagnosis_ctrl = ctrl.ControlSystem(rules)
diagnosis = ctrl.ControlSystemSimulation(diagnosis_ctrl)

def run_fuzzy_diagnosis(df: pd.DataFrame) -> pd.DataFrame:
    results = []
    for idx, row in df.iterrows():
        try:
            for sym in symptom_names:
                diagnosis.input[sym] = float(row[sym])
            diagnosis.compute()
            results.append(diagnosis.output['disease'])
        except Exception:
            results.append(np.nan)
    df_out = df.copy()
    df_out['Fuzzy Disease Score'] = results
    return df_out
