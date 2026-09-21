#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from utils_final import CATEGORIES, clean_name, load_sequence_csv, normalized_levenshtein, padded_mismatch, jaccard_binary

def build(df, seqs, metric):
    df = df.copy()
    df["canonical"] = df["canonical"].map(clean_name)
    if df["canonical"].duplicated().any():
        raise ValueError("Canonical matrix contains duplicated mature-sequence tips.")
    names = df["canonical"].tolist()
    missing = [n for n in names if n not in seqs]
    if missing:
        raise ValueError(f"Missing exact mature sequences: {missing}")
    n = len(names)
    S = np.zeros((n,n)); F = np.zeros((n,n))
    for i in range(n):
        for j in range(i+1,n):
            S[i,j] = S[j,i] = metric(seqs[names[i]], seqs[names[j]])
            F[i,j] = F[j,i] = jaccard_binary(df.loc[i,CATEGORIES], df.loc[j,CATEGORIES])
    return names, S, F

def test(S, F, permutations=5000, seed=42):
    iu = np.triu_indices_from(S, 1)
    x, y = S[iu], F[iu]
    rho = float(spearmanr(x,y).statistic)
    rng = np.random.default_rng(seed)
    null = np.empty(permutations)
    for k in range(permutations):
        p = rng.permutation(S.shape[0])
        null[k] = spearmanr(x, F[np.ix_(p,p)][iu]).statistic
    pval = (np.sum(np.abs(null) >= abs(rho)) + 1) / (permutations + 1)
    return rho, float(pval), null

def run_one(label, matrix, seqs, outdir, permutations, seed):
    df = pd.read_csv(matrix)
    rows = []
    for metric_name, fn in [("Normalized Levenshtein", normalized_levenshtein), ("Padded mismatch sensitivity", padded_mismatch)]:
        names,S,F = build(df,seqs,fn)
        rho,p,null = test(S,F,permutations,seed)
        rows.append({"Dataset":label,"Sequence metric":metric_name,"n_miRNAs":len(names),"pairwise_comparisons":len(names)*(len(names)-1)//2,"Spearman_rho":rho,"permutation_p_two_sided":p,"permutations":permutations,"seed":seed})
        if metric_name == "Normalized Levenshtein":
            pd.DataFrame(S,index=names,columns=names).to_csv(outdir/f"{label}_sequence_distance.csv",index_label="miRNA")
            pd.DataFrame(F,index=names,columns=names).to_csv(outdir/f"{label}_disease_profile_distance.csv",index_label="miRNA")
            pd.DataFrame({"permuted_rho":null}).to_csv(outdir/f"{label}_null_distribution.csv",index=False)
    return rows

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--all-matrix",type=Path,required=True)
    p.add_argument("--e1-matrix",type=Path,required=True)
    p.add_argument("--sequences",type=Path,required=True)
    p.add_argument("--outdir",type=Path,default=Path("results/final"))
    p.add_argument("--permutations",type=int,default=5000)
    p.add_argument("--seed",type=int,default=42)
    a=p.parse_args(); a.outdir.mkdir(parents=True,exist_ok=True)
    seqs=load_sequence_csv(a.sequences)
    rows=[]
    rows += run_one("ALL",a.all_matrix,seqs,a.outdir,a.permutations,a.seed)
    rows += run_one("E1-only",a.e1_matrix,seqs,a.outdir,a.permutations,a.seed)
    stats=pd.DataFrame(rows)
    stats.to_csv(a.outdir/"Figure8_final_statistics_recomputed.csv",index=False)
    print(stats.to_string(index=False))
if __name__=="__main__": main()
