import unittest
import os
import pandas as pd
from tcga_immune.profiler import calculate_cohort_immune_summary, calculate_checkpoint_correlation

class TestTCGAImmuneProfiler(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.csv_path = os.path.join(
            os.path.dirname(__file__), "..", "examples", "data", "tcga_pancancer_immune_subtypes.csv"
        )
        cls.df = pd.read_csv(cls.csv_path)

    def test_dataset_loading(self):
        self.assertEqual(len(self.df), 30)
        self.assertEqual(len(self.df["cohort"].unique()), 3)

    def test_cohort_summary_numerical_accuracy(self):
        summary = calculate_cohort_immune_summary(self.df)
        
        # TCGA-SKCM assertions
        skcm = summary["TCGA-SKCM"]
        self.assertEqual(skcm["sample_count"], 10)
        self.assertAlmostEqual(skcm["mean_cd8_t_cells"], 0.2820, places=4)
        self.assertAlmostEqual(skcm["mean_pdl1_tpm"], 6.55, places=2)
        
        # TCGA-LUAD assertions
        luad = summary["TCGA-LUAD"]
        self.assertAlmostEqual(luad["mean_cd8_t_cells"], 0.1720, places=4)
        self.assertAlmostEqual(luad["mean_pdl1_tpm"], 4.16, places=2)
        
        # TCGA-BRCA assertions
        brca = summary["TCGA-BRCA"]
        self.assertAlmostEqual(brca["mean_cd8_t_cells"], 0.1150, places=4)
        self.assertAlmostEqual(brca["mean_pdl1_tpm"], 3.19, places=2)

    def test_checkpoint_correlation_numerical_accuracy(self):
        corr = calculate_checkpoint_correlation(self.df)
        self.assertAlmostEqual(corr["pearson_r"], 0.9915, places=4)
        self.assertAlmostEqual(corr["r_squared"], 0.9832, places=4)

if __name__ == '__main__':
    unittest.main()
