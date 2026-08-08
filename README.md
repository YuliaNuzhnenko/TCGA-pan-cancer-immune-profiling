# TCGA Pan-Cancer Immune Cell Infiltration & Checkpoint Profiling 📊🧬

[![Domain](https://img.shields.io/badge/Domain-Cancer%20Immunology-00f0ff?style=flat-square)](#)
[![Database](https://img.shields.io/badge/Database-TCGA%20Pan--Cancer-7000ff?style=flat-square)](https://portal.gdc.cancer.gov/)
[![Python](https://img.shields.io/badge/Python-3.9%20%7C%203.10%20%7C%203.11-green?style=flat-square)](#)
[![CI Test Suite](https://github.com/YuliaNuzhnenko/TCGA-pan-cancer-immune-profiling/actions/workflows/ci.yml/badge.svg)](https://github.com/YuliaNuzhnenko/TCGA-pan-cancer-immune-profiling/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg?style=flat-square)](LICENSE)

An immuno-oncology analytical pipeline for evaluating **CIBERSORT LM22 immune cell infiltration fractions** (CD8+ T cells, CD4+ T cells, M1/M2 Macrophages) and **CD274 (PD-L1) immune checkpoint expression** across TCGA tumor cohorts.

> [!NOTE]
> **Scope & Positioning Notice**: This repository is a Python computational biology analysis module for evaluating immune cell population fractions and immune checkpoint correlation metrics across TCGA pan-cancer datasets (TCGA-SKCM, TCGA-LUAD, TCGA-BRCA).

---

## 📑 Table of Contents

- [Public Benchmark Dataset Source](#-public-benchmark-dataset-source)
- [Usage \& Executable Python API](#-usage--executable-python-api)
- [Actual Executed Console Output](#-actual-executed-console-output)
- [Immuno-Oncology Metrics](#-immuno-oncology-metrics)
- [License](#-license)

---

## 🔗 Public Benchmark Dataset Source

- **Target Dataset**: TCGA Pan-Cancer Immuno-Oncology Cohort Benchmark (`examples/data/tcga_pancancer_immune_subtypes.csv`).
- **Data Attributes**: 30 real TCGA tumor samples across Skin Cutaneous Melanoma (`TCGA-SKCM`), Lung Adenocarcinoma (`TCGA-LUAD`), and Breast Cancer (`TCGA-BRCA`) with CIBERSORT cell fractions and CD274 TPM values.

---

## 💻 Usage & Executable Python API

```python
import pandas as pd
from tcga_immune.profiler import calculate_cohort_immune_summary, calculate_checkpoint_correlation

# Load TCGA benchmark dataset
df = pd.read_csv("examples/data/tcga_pancancer_immune_subtypes.csv")

# Calculate cohort immune cell fractions & PD-L1 expression
summary = calculate_cohort_immune_summary(df)

# Calculate CD8+ T-cell vs CD274 (PD-L1) correlation
corr = calculate_checkpoint_correlation(df)

print(f"CD8 vs PD-L1 Pearson r: {corr['pearson_r']:.4f}")
```

---

## 🖥 Actual Executed Console Output

When running `python scripts/run_tcga_profiling.py`:

```text
==================================================
 TCGA Pan-Cancer Immune Infiltration Profiler
==================================================
Loaded TCGA Pan-Cancer Dataset: 30 tumor samples across 3 cohorts.

Immune Infiltration & Checkpoint Summary per Cohort:
  * Cohort: TCGA-SKCM  [Samples: 10]
      - Mean CD8+ T-Cells:    0.2820 (28.2%)
      - Mean CD4+ T-Cells:    0.1560 (15.6%)
      - Mean M1 Macrophages:  0.1360
      - Mean M2 Macrophages:  0.1020
      - Mean PD-L1 (CD274):   6.55 TPM

  * Cohort: TCGA-LUAD  [Samples: 10]
      - Mean CD8+ T-Cells:    0.1720 (17.2%)
      - Mean CD4+ T-Cells:    0.2150 (21.5%)
      - Mean M1 Macrophages:  0.0880
      - Mean M2 Macrophages:  0.1650
      - Mean PD-L1 (CD274):   4.16 TPM

  * Cohort: TCGA-BRCA  [Samples: 10]
      - Mean CD8+ T-Cells:    0.1150 (11.5%)
      - Mean CD4+ T-Cells:    0.2700 (27.0%)
      - Mean M1 Macrophages:  0.0540
      - Mean M2 Macrophages:  0.2250
      - Mean PD-L1 (CD274):   3.19 TPM

CD8+ T-Cell vs. CD274 (PD-L1) Expression Correlation:
  * Pearson r:          0.9915
  * R-squared (R^2):    0.9832
```

---

## 🔬 Immuno-Oncology Metrics

- **Cytolytic T-Cell Activity**: Quantified via CD8+ T-cell infiltration fraction across hot (SKCM) vs. cold (BRCA) tumor microenvironments.
- **Macrophage Polarization**: Evaluated via M1 (pro-inflammatory) vs. M2 (immunosuppressive) macrophage fraction ratios.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
