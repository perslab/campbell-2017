#!/usr/bin/python

import pandas as pd
import glob,pdb,os,sys
import numpy as np

# Determine and set path
path_to_script = os.path.realpath(__file__).split('/')
path = "/".join(path_to_script[0:(len(path_to_script)-2)])
sys.path.append("{}/src/python-armory".format(path))
from gene_mapping import to_ensembl

# Filenames and global variables
timestamp = 160129
mapping_mm_mm_file = "{}/data/mapping/ensembl_v83_ensembl_mgisymbol_Mm.tab.gz".format(path)
mapping_mm_hs_file = "{}/data/mapping/ensembl_v82_Mm_Hs.tab.gz".format(path)
mouse_celltype_file = "{}/data/initial/NeuronData_average.txt.gz".format(path)
human_celltype_file = "{}/data/initial/{}_by_celltype.tab".format(path,timestamp)


# Mouse to human gene mapping
df_mm2mm = pd.read_csv(mapping_mm_mm_file,compression="gzip",index_col=1,sep="\t")
df_mm2mm = df_mm2mm[[isinstance(x, str) for x in df_mm2mm.index]] # Discard nan entries
df_mm2hs = pd.read_csv(mapping_mm_hs_file,compression="gzip",index_col=0,sep="\t")

# Read data
df_mm = pd.read_csv(mouse_celltype_file,sep="\t",index_col=0,header=0,compression="gzip")

# Map to human
df_hs,not_mapped = to_ensembl(df_mm2mm,df_mm2hs,df_mm)
pdb.set_trace()

# Save
df_hs.to_csv(human_celltype_file,index=True,header=True,sep="\t")
