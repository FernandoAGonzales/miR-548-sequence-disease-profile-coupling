# v1.0.0-submission

**Release date:** 2026-09-29  
**Status:** Manuscript-submission snapshot

This release is the audited, submission-synchronized computational record for the manuscript:

**Disease-association convergence in the miR-548 family reveals limited coupling between mature-sequence evolution and broad disease profiles**

## Included in this release

- Eight manuscript figures in `Figures/` (`Figure1.png` through `Figure8.png`).
- Final curated disease-association tables in `data/final/`.
- Mature miR-548 sequence resources and alignment in `data/raw/`.
- Final Figure 7 disease-association architecture outputs in `results/final/`.
- Final Figure 8 sequence–disease-profile analyses, null distribution, and sensitivity analyses in `results/final/`.
- Locked phylogenetic resources in `results/phylogeny/`.
- Audited Figure 7/8 analysis scripts in `scripts/final_audited_workflow/`.
- Figure 6 sequence-alignment and Shannon-entropy scripts in `scripts/scripts for figure 6/`.
- Reproducibility metadata, environment files, citation metadata, manifest, and checksums.

## Final analysis populations

- Figure 5 phylogeny: 81 mature sequences (37 3p-derived; 44 5p-derived), K2P+G, 2,000 bootstrap replicates, 34 aligned positions.
- Figure 7 descriptive disease architecture: 54 curated disease identifiers.
- Figure 8 primary sequence-resolved analysis: 44 unique mature-sequence tips and 946 pairwise comparisons.
- Figure 8 E1-only sensitivity analysis: 43 unique mature-sequence tips and 903 pairwise comparisons.

Seven generic arm-unspecified disease identifiers are retained in descriptive disease evidence but excluded from analyses that require a unique mature sequence.

Three nomenclature aliases are collapsed in sequence-resolved analyses:

- `miR-548ac-3p -> miR-548ac`
- `miR-548l-5p -> miR-548l`
- `miR-548s-3p -> miR-548s`

## Final Figure 8 statistics

| Analysis | n | pairs | Spearman rho | permutation p |
|---|---:|---:|---:|---:|
| ALL, normalized Levenshtein | 44 | 946 | -0.1103 | 0.1002 |
| E1-only, normalized Levenshtein | 43 | 903 | -0.1150 | 0.1008 |
| ALL, padded-mismatch sensitivity | 44 | 946 | -0.0862 | 0.2412 |
| E1-only, padded-mismatch sensitivity | 43 | 903 | -0.0863 | 0.2583 |

The submission-snapshot conclusion is that no detectable positive coupling is observed between mature-sequence distance and the four-category disease-profile distance, and this conclusion is stable to E1-only filtering and the alternative padded-mismatch sequence metric.

## Evidence scope

The curated disease-association table contains 134 records. E1 denotes published experimental support in the cited literature for the corresponding miRNA–disease association; it does not represent new wet-laboratory validation performed in this manuscript.

## Snapshot policy

Superseded draft disease tables, legacy Figure 7/8 workflows, and obsolete processed outputs are intentionally excluded from this public submission snapshot to avoid confusion with the audited final analyses.

## Archival

After the GitHub tag/release is frozen, this release is intended for Zenodo archival. The resulting DOI should then be added to the manuscript Data Availability Statement and repository citation metadata.
