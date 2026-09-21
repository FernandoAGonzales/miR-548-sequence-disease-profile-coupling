# Final audited workflow

This directory is the authoritative reproducible workflow for the submitted analysis.

## Analysis populations

- Figure 5 phylogeny: 81 mature miR-548 sequences.
- Figure 7 descriptive disease architecture: 54 curated disease identifiers.
- Figure 8 primary sequence-resolved analysis: 44 unique mature-sequence tips.
- Figure 8 E1-only sensitivity analysis: 43 unique mature-sequence tips.

The intermediate 47/46 disease-identifier counts are **not** treated as independent mature sequences because three nomenclature aliases map to single deposited mature-sequence tips:

- miR-548ac-3p -> miR-548ac
- miR-548l-5p -> miR-548l
- miR-548s-3p -> miR-548s

Generic arm-unspecified disease identifiers are retained in descriptive disease analyses but are not mapped automatically to a 3p/5p sequence.

## Final sequence-function analysis

Primary sequence distance: normalized global Levenshtein distance.
Functional/disease-profile distance: Jaccard distance across Cancer, Infectious diseases, Inflammatory diseases, and Autoimmune diseases.
Permutation test: 5,000 miRNA-label permutations, seed 42, two-sided by absolute Spearman rho.

Expected final results:

| Dataset | n | pairs | rho | p |
|---|---:|---:|---:|---:|
| ALL | 44 | 946 | -0.1103 | 0.1002 |
| E1-only | 43 | 903 | -0.1150 | 0.1008 |
| ALL padded-mismatch sensitivity | 44 | 946 | -0.0862 | 0.2412 |
| E1-only padded-mismatch sensitivity | 43 | 903 | -0.0863 | 0.2583 |

Run `sequence_function_final.py` to regenerate the numerical outputs and `generate_figure7_final.py` to regenerate the descriptive Figure 7 data visualization.
