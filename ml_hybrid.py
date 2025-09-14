import pandas as pd
import numpy as np

def run_ml_prediction(df: pd.DataFrame) -> pd.DataFrame:
    # Placeholder ML risk model: normalized sum of symptoms
    df_out = df.copy()
    df_out['ML Risk Score'] = df.sum(axis=1) / len(df.columns) * 10
    return df_out
