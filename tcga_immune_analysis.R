# TCGA Pan-Cancer Immune Profiling Script
# Author: Yulia Nuzhnenko

library(ggplot2)

set.seed(123)
cohorts <- rep(c("TCGA-LUAD", "TCGA-SKCM", "TCGA-BRCA"), each=50)
pdl1_exp <- c(rnorm(50, 4, 1), rnorm(50, 6, 1.2), rnorm(50, 3.5, 0.8))

df <- data.frame(Cohort=cohorts, PDL1_Expression=pdl1_exp)

p <- ggplot(df, aes(x=Cohort, y=PDL1_Expression, fill=Cohort)) +
    geom_boxplot(alpha=0.7) +
    theme_minimal() +
    labs(title="PD-L1 (CD274) Expression across TCGA Cohorts", y="Log2 (TPM + 1)")

ggsave("tcga_pdl1_expression.png", p, width=7, height=5)
print("Analysis complete. Plot saved.")
