#!/usr/bin/python

import pandas as pd
import glob,pdb,os,sys
import numpy as np

# Determine and set path
path_to_script = os.path.realpath(__file__).split('/')
path = "/".join(path_to_script[0:(len(path_to_script)-2)])
sys.path.append("{}/src/depict-sc-library".format(path))
from gene_mapping import to_ensembl 
from dropseq import get_clusters,get_average_by_celltype,standardize,normalize

# Filenames and global variables
timestamp = 160219
mapping_mm_mm_file = "{}/data/mapping/ensembl_v83_ensembl_mgisymbol_Mm.tab.gz".format(path)
mapping_mm_hs_file = "{}/data/mapping/ensembl_v82_Mm_Hs.tab.gz".format(path)
mouse_celltype_file = "{}/data/initial/NeuronData_average.txt.gz".format(path)
human_celltype_file = "{}/data/initial/{}_neurons_celltype.tab".format(path,timestamp)

# Mouse to human gene mapping
df_mm2mm = pd.read_csv(mapping_mm_mm_file,compression="gzip",index_col=1,sep="\t")
df_mm2mm = df_mm2mm[[isinstance(x, str) for x in df_mm2mm.index]] # Discard nan entries
df_mm2hs = pd.read_csv(mapping_mm_hs_file,compression="gzip",index_col=0,sep="\t")

# Read data
df_raw = pd.read_csv(mouse_celltype_file,sep="\t",index_col=0,header=0,compression="gzip")

# Normalize
df_nm = normalize(df_raw)

# Map to human
df_hs,not_mapped = to_ensembl(df_mm2mm,df_mm2hs,df_nm)

# Standardize genes' expresion across tissues
df_hs_st = standardize(df_hs)

# Save
df_hs.to_csv(human_celltype_file,index=True,header=True,sep="\t")
df_hs_st.to_csv(human_celltype_standardized_file,index=True,header=True,sep="\t")
