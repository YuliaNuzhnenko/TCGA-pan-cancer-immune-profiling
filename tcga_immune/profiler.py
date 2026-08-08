import numpy as np
import pandas as pd

def calculate_cohort_immune_summary(df):
    """
    Calculates mean immune cell infiltration fractions (CD8 T cells, CD4 T cells, M1/M2 Macrophages)
    and mean PD-L1 (CD274) TPM expression across TCGA tumor cohorts.
    """
    summary = {}
    cohorts = df["cohort"].unique()
    
    for c in cohorts:
        cdf = df[df["cohort"] == c]
        summary[c] = {
            "sample_count": len(cdf),
            "mean_cd8_t_cells": float(cdf["CD8_T_cells"].mean()),
            "mean_cd4_t_cells": float(cdf["CD4_T_cells"].mean()),
            "mean_m1_macrophages": float(cdf["M1_Macrophages"].mean()),
            "mean_m2_macrophages": float(cdf["M2_Macrophages"].mean()),
            "mean_pdl1_tpm": float(cdf["CD274_PDL1_TPM"].mean())
        }
    return summary

def calculate_checkpoint_correlation(df):
    """
    Calculates Pearson correlation coefficient between CD8+ T-cell infiltration fraction
    and CD274 (PD-L1) expression across all tumor samples.
    """
    x = df["CD8_T_cells"].values
    y = df["CD274_PDL1_TPM"].values
    
    n = len(x)
    if n < 2:
        return {"pearson_r": 0.0, "r_squared": 0.0}
        
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    num = np.sum((x - mean_x) * (y - mean_y))
    den = np.sqrt(np.sum((x - mean_x)**2) * np.sum((y - mean_y)**2))
    
    r = float(num / den) if den > 0 else 0.0
    return {
        "pearson_r": r,
        "r_squared": float(r**2),
        "sample_size": n
    }
