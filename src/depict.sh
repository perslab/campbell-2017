#! /bin/sh

flag_study=height_wood
#flag_study=scz_ripke
#flag_study=whr_shungin
#flag_study=bmi_locke
flag_norm="" #_standardized
flag_cells=allcells #allneurons 

qsub -q short -e ../log/depict_${flag_study}${flag_norm}.err -o ../log/depict_${flag_study}${flag_norm}.out -cwd -l m_mem_free=16g /cvar/jhlab/tp/depict/src/python/broad_run.sh python /cvar/jhlab/tp/depict/src/python/depict.py /cvar/jhlab/tp/drop-seq/campbell-2016/src/${flag_study}_${flag_cells}${flag_norm}.cfg
