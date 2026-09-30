# Disease-association convergence in the miR-548 family

This repository is the audited, submission-synchronized computational record for the manuscript:

**Disease-association convergence in the miR-548 family reveals limited coupling between mature-sequence evolution and broad disease profiles**

Repository: `https://github.com/FernandoAGonzales/miR-548-sequence-disease-profile-coupling`

Zenodo archival release: `v1.0.1-submission`  
DOI: **10.5281/zenodo.23048837**

## Final analysis populations

- **Figure 5:** locked maximum-likelihood phylogeny of 81 mature miR-548 sequences (37 3p-derived; 44 5p-derived), K2P+G, 2,000 bootstrap replicates, 34 aligned positions.
- **Figure 7:** descriptive disease-association architecture using all 54 curated disease identifiers.
- **Figure 8:** sequence-resolved analysis using 44 unique mature-sequence tips after exact sequence matching and collapse of three nomenclature aliases. E1-only sensitivity uses 43 unique mature-sequence tips.

Seven generic arm-unspecified disease identifiers are retained in descriptive disease evidence but excluded from analyses requiring a unique mature sequence. No automatic generic-to-arm fallback is permitted.

Three nomenclature aliases are collapsed onto their single deposited mature-sequence tips in sequence-resolved analyses:

- `miR-548ac-3p -> miR-548ac`
- `miR-548l-5p -> miR-548l`
- `miR-548s-3p -> miR-548s`

## Authoritative final data

Use `data/final/` for manuscript-facing analyses.

- `Supplementary_Data_S1_Curated_miR548_disease_association_table_FINAL.csv` — 134 record-level curated disease associations.
- `Supplementary_Table_S1_Autoimmune_FINAL.csv` — publication-facing autoimmune summary.
- `Supplementary_Table_S2_Infectious_Inflammatory_FINAL.csv` — publication-facing infectious/inflammatory summary.
- `Supplementary_Table_S3_Cancer_FINAL.csv` — 40 named neoplastic conditions/subtypes; the generic `Cancer` record is not counted as a named condition.
- `Table1_Experimentally_validated_miRNA_target_interactions_FINAL.csv` — the 40 E1 records containing a curated `Validated_targets` entry; source for manuscript Table 1.
- `binary_disease_matrix_54_identifiers_FINAL.csv` — 54-identifier descriptive matrix used for Figure 7.
- `Figure8_ALL_canonical_44_miRNAs.csv` — final primary sequence-resolved matrix.
- `Figure8_E1only_canonical_43_miRNAs.csv` — final E1-only sequence-resolved matrix.
- `miR548_FINAL_Supplementary_Tables_S1_S3_and_Figure2_3_audit.xlsx` — reconciled supplementary workbook plus Figure 2/3 source audit.

The mature-sequence repertoire and exact deposited alignment are retained in `data/raw/` as sequence source resources. Superseded draft disease tables and legacy processed outputs are intentionally excluded from this public submission snapshot.

## Figures 2 and 3

The final manuscript artwork is provided in `Figures/`.

- **Figure 2:** anatomical overview of 24 named non-cancer conditions represented in final Supplementary Tables S1-S2.
- **Figure 3:** anatomical overview of 40 named neoplastic conditions/subtypes represented in final Supplementary Table S3.

## Final Figure 7

Figure 7 describes broad disease-association architecture, not phylogeny.

- Panel A: binary disease-profile matrix; rows are ordered using Jaccard distance and average-linkage clustering, while the dendrogram is omitted to avoid visual redundancy with Figure 5.
- Panel B: bipartite miRNA-disease-category network.
- Panel C: disease-category intersection analysis.

Category-presence counts across 54 identifiers:

- Cancer: 46
- Infectious diseases: 13
- Inflammatory diseases: 12
- Autoimmune diseases: 6

## Final Figure 8

Primary sequence distance is normalized global Levenshtein distance. Disease-profile distance is Jaccard distance over four binary disease categories. Statistical significance is assessed with 5,000 label permutations using seed 42.

| Analysis | n | pairs | Spearman rho | permutation p |
|---|---:|---:|---:|---:|
| ALL, normalized Levenshtein | 44 | 946 | -0.1103 | 0.1002 |
| E1-only, normalized Levenshtein | 43 | 903 | -0.1150 | 0.1008 |
| ALL, padded-mismatch sensitivity | 44 | 946 | -0.0862 | 0.2412 |
| E1-only, padded-mismatch sensitivity | 43 | 903 | -0.0863 | 0.2583 |

**Conclusion:** no detectable positive sequence-disease-profile coupling. This conclusion is stable to E1-only filtering and to the alternative padded-mismatch sequence metric.

## Final manuscript figures

`Figures/` contains the eight manuscript figure PNGs as `Figure1.png` through `Figure8.png`.

## Reproducibility

The authoritative Figure 7/8 scripts are in `scripts/final_audited_workflow/`.

The Figure 6 sequence-alignment and Shannon-entropy scripts are in `scripts/scripts for figure 6/`.

Legacy workflows and superseded processed outputs are intentionally excluded from this public submission snapshot to avoid confusion with the audited final analyses.

## Phylogenetic resources

`results/phylogeny/` contains the deposited maximum-likelihood tree and MEGA analysis resources. The final Figure 5 is based on this locked phylogeny; phylogenetic inference was not rerun during the disease-association audit.

## Software

Python 3.12; NumPy; pandas; SciPy; NetworkX; matplotlib; Biopython. MEGA v12.1 was used for phylogenetic reconstruction.

## Archival release

The submission-synchronized archival snapshot is GitHub release `v1.0.1-submission`, permanently preserved in Zenodo under DOI **10.5281/zenodo.23048837**.
