#! /usr/bin/python

import pdb

depict_bim_file = "/cvar/jhlab/tp/depict/data/genotype_data_plink/CEU_GBR_TSI_unrelated.phase1_release_v3.20101123.snps_indels_svs.genotypes_noduplicates.bim"
bim_chr_col = 0
bim_id_col = 1
bim_pos_col = 3

# T2D
gwas_infile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/mahaja_t2d/DIAGRAMv3.2012DEC17.txt"
gwas_outfile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/mahaja_t2d/DIAGRAMv3.2012DEC17_chrpos.txt"
gwas_id_col = 0
gwas_p_col = 5

# Menarche
gwas_infile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/perry_menarche/Menarche_Nature2014_GWASMetaResults_17122014.txt"
gwas_outfile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/perry_menarche/Menarche_Nature2014_GWASMetaResults_17122014_chrpos.tab"
gwas_id_col = 0
gwas_p_col = 5

# Menopause
gwas_infile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/day_menopause/Menopause_HapMap2_DayNG2015_18112015.txt"
gwas_outfile = "/cvar/jhlab/tp/drop-seq/campbell-2016/data/gwas/day_menopause/Menopause_HapMap2_DayNG2015_18112015_chrpos.tab"
gwas_id_col = 0
gwas_p_col = 6


# Read mappings
with open(depict_bim_file,'r') as infile:
	lines = infile.readlines()
	mapping = {}
	for line in lines:
		words = line.strip().split()
		mapping[words[bim_id_col]] = "%s:%s"%(words[bim_chr_col],words[bim_pos_col])

# Re-map
with open(gwas_infile,'r') as infile: 
	lines = infile.readlines()
	with open(gwas_outfile,'w') as outfile: 
		outfile.write("SNP\tStudy_ID\tP\n")
		for line in lines[1:]:
			words = line.strip().split()
			if words[gwas_id_col] in mapping:
				outfile.write("%s\t%s\t%s\n"%(mapping[words[gwas_id_col]],words[gwas_id_col],words[gwas_p_col]))
