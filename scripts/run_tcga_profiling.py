#!/usr/bin/env python3
"""
TCGA Pan-Cancer Immune Infiltration & Checkpoint Profiler
Author: Yulia Nuzhnenko
"""
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import pandas as pd
from tcga_immune.profiler import calculate_cohort_immune_summary, calculate_checkpoint_correlation

def main():
    print("==================================================")
    print(" TCGA Pan-Cancer Immune Infiltration Profiler")
    print("==================================================")
    csv_path = os.path.join(os.path.dirname(__file__), "..", "examples", "data", "tcga_pancancer_immune_subtypes.csv")
    df = pd.read_csv(csv_path)
    
    print(f"Loaded TCGA Pan-Cancer Dataset: {len(df)} tumor samples across {len(df['cohort'].unique())} cohorts.\n")
    summary = calculate_cohort_immune_summary(df)
    
    print("Immune Infiltration & Checkpoint Summary per Cohort:")
    for cohort, m in summary.items():
        print(f"  * Cohort: {cohort:<10} [Samples: {m['sample_count']}]")
        print(f"      - Mean CD8+ T-Cells:    {m['mean_cd8_t_cells']:.4f} ({m['mean_cd8_t_cells']*100:.1f}%)")
        print(f"      - Mean CD4+ T-Cells:    {m['mean_cd4_t_cells']:.4f} ({m['mean_cd4_t_cells']*100:.1f}%)")
        print(f"      - Mean M1 Macrophages:  {m['mean_m1_macrophages']:.4f}")
        print(f"      - Mean M2 Macrophages:  {m['mean_m2_macrophages']:.4f}")
        print(f"      - Mean PD-L1 (CD274):   {m['mean_pdl1_tpm']:.2f} TPM\n")
        
    corr = calculate_checkpoint_correlation(df)
    print(f"CD8+ T-Cell vs. CD274 (PD-L1) Expression Correlation:")
    print(f"  * Pearson r:          {corr['pearson_r']:.4f}")
    print(f"  * R-squared (R^2):    {corr['r_squared']:.4f}")

if __name__ == "__main__":
    main()
