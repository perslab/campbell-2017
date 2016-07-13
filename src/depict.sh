#! /bin/sh

path=/cvar/jhlab/tp/drop-seq/campbell-2016
data_flag=160603
results_flag=160704
phenotypes=( bmi_locke ) #menarche_perry menopause_day t2d_mahaja whr_shungin height_wood anorexia_boraska scz_ripke )

flag_cells=(neuron) #allcellclustered allcellmicrocluster neuron_arconly ) 
flag_norms=("") #_std 

for pheno in "${phenotypes[@]}"
do
	for flag_cell in "${flag_cells[@]}"
	do
		for flag_norm in "${flag_norms[@]}"
		do
			qsub -q short -e $path/log/depict_${pheno}_${flag_cell}${flag_norm}.err -o $path/log/depict_${pheno}_${flag_cell}${flag_norm}.out -cwd -l m_mem_free=16g /cvar/jhlab/tp/depict/src/python/broad_run.sh python /cvar/jhlab/tp/depict/src/python/depict.py $path/data/$data_flag/results_$results_flag/${pheno}_${flag_cell}${flag_norm}.cfg
		done
	done
done
