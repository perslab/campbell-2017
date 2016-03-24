#!/usr/bin/python

import pandas as pd
import glob,pdb,os,sys
import numpy as np

# Determine and set path
path_to_script = os.path.realpath(__file__).split('/')
path = "/".join(path_to_script[0:(len(path_to_script)-2)])
sys.path.append("{}/src/perslab-sc-library".format(path))
from gene_mapping import to_ensembl 
from dropseq import standardize

# Filenames and global variables
timestamp = 160324
#label = "Allcell_020816_BC_clustered1"
#label = "Allcell_020816_BC_microcluster"
label = "Allneuron_35PC_clusters"
mapping_mm_mm_file = "{}/data/mapping/ensembl_v83_ensembl_mgisymbol_Mm.tab.gz".format(path)
mapping_mm_hs_file = "{}/data/mapping/ensembl_v82_Mm_Hs.tab.gz".format(path)
mouse_cellclusters_file = "{}/data/{}/{}_Data_average.txt.gz".format(path,timestamp,label)
human_cellclusters_file = "{}/data/{}/{}_{}_cellclusters.tab".format(path,timestamp,timestamp,label)
human_cellclusters_standardized_file = "{}/data/{}/{}_{}_cellclusters_standardized.tab".format(path,timestamp,timestamp,label)

# Mouse to human gene mapping
df_mm2mm = pd.read_csv(mapping_mm_mm_file,compression="gzip",index_col=1,sep="\t")
df_mm2mm = df_mm2mm[[isinstance(x, str) for x in df_mm2mm.index]] # Discard nan entries
df_mm2hs = pd.read_csv(mapping_mm_hs_file,compression="gzip",index_col=0,sep="\t")

# Read data
df_mm_cellclusters = pd.read_csv(mouse_cellclusters_file,sep="\t",index_col=0,header=0,compression="gzip")

# Normalize
#df_nm = normalize(df_raw)

# Average cells by cluster
#df_cluster = get_clusters(cluster_file,True,False)
#df_mm_cellclusters = get_average_by_celltype(df_nm,df_cluster)

# Map to human
df_hs,not_mapped = to_ensembl(df_mm2mm,df_mm2hs,df_mm_cellclusters)

# Standardize genes' expresion across tissues
df_hs_st = standardize(df_hs)

# Save
df_hs.to_csv(human_cellclusters_file,index=True,header=True,sep="\t")
df_hs_st.to_csv(human_cellclusters_standardized_file,index=True,header=True,sep="\t")
