#!/usr/bin/env python3
from __future__ import annotations
import argparse
from pathlib import Path
from collections import Counter
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from scipy.cluster.hierarchy import linkage, leaves_list
from scipy.spatial.distance import pdist
from utils_final import CATEGORIES

def main():
    p=argparse.ArgumentParser(); p.add_argument("--matrix",type=Path,required=True); p.add_argument("--outdir",type=Path,default=Path("figures/final")); a=p.parse_args(); a.outdir.mkdir(parents=True,exist_ok=True)
    df=pd.read_csv(a.matrix)
    if len(df)!=54: raise ValueError(f"Expected 54 descriptive identifiers, found {len(df)}")
    X=df[CATEGORIES].astype(int).values
    Z=linkage(pdist(X,metric="jaccard"),method="average",optimal_ordering=True)
    ordered=df.iloc[leaves_list(Z)].reset_index(drop=True)
    fig=plt.figure(figsize=(16,10)); gs=fig.add_gridspec(2,2,width_ratios=[0.9,1.1],height_ratios=[1.0,0.75],wspace=.28,hspace=.30)
    # A matrix only, avoiding visual redundancy with Figure 5.
    ax=fig.add_subplot(gs[:,0]); M=ordered[CATEGORIES].values
    for i in range(len(ordered)):
        for j,c in enumerate(CATEGORIES):
            if M[i,j]: ax.scatter(j,i,marker="s",s=22)
    ax.set_yticks(range(len(ordered))); ax.set_yticklabels(ordered.miRNA,fontsize=5.8); ax.set_xticks(range(4)); ax.set_xticklabels(CATEGORIES,rotation=35,ha="left",fontsize=8); ax.xaxis.tick_top(); ax.invert_yaxis(); ax.set_title("A  Disease-profile matrix ordered by Jaccard/average-linkage clustering",loc="left",fontweight="bold")
    for s in ax.spines.values(): s.set_visible(False)
    # B network
    bx=fig.add_subplot(gs[0,1]); G=nx.Graph()
    for c in CATEGORIES: G.add_node(c,kind="category")
    for _,r in ordered.iterrows():
        G.add_node(r.miRNA,kind="miRNA")
        for c in CATEGORIES:
            if int(r[c]): G.add_edge(r.miRNA,c)
    pos=nx.spring_layout(G,seed=42,k=0.55,iterations=300)
    nx.draw_networkx_edges(G,pos,ax=bx,alpha=.18,width=.6)
    nx.draw_networkx_nodes(G,pos,nodelist=ordered.miRNA.tolist(),node_size=16,ax=bx)
    nx.draw_networkx_nodes(G,pos,nodelist=CATEGORIES,node_size=700,ax=bx)
    nx.draw_networkx_labels(G,pos,labels={c:c for c in CATEGORIES},font_size=7,ax=bx)
    bx.set_title("B  miRNA–disease-category network",loc="left",fontweight="bold"); bx.axis("off")
    # C intersections
    cx=fig.add_subplot(gs[1,1]); pat=Counter(tuple(map(int,row)) for row in ordered[CATEGORIES].values); items=sorted(pat.items(),key=lambda kv:-kv[1]); vals=[v for _,v in items]; cx.bar(range(len(vals)),vals); cx.set_ylabel("Number of miRNAs"); cx.set_xticks(range(len(vals))); cx.set_xticklabels(["" for _ in vals]); cx.set_title("C  Disease-category overlap",loc="left",fontweight="bold")
    for i,v in enumerate(vals): cx.text(i,v+.15,str(v),ha="center",fontsize=8)
    fig.suptitle("Figure 7. Disease-association architecture of the miR-548 family",fontweight="bold",y=.98)
    fig.savefig(a.outdir/"Figure7_recomputed.pdf",bbox_inches="tight")
    fig.savefig(a.outdir/"Figure7_recomputed.png",dpi=600,bbox_inches="tight")
    ordered.to_csv(a.outdir/"Figure7A_ordered_matrix_recomputed.csv",index=False)
if __name__=="__main__": main()
