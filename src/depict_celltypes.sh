#! /bin/sh

qsub -q short -e ../log/celltypes.err -o ../log/celltypes.out -cwd -l m_mem_free=12g /cvar/jhlab/tp/DEPICT/src/python/broad_run.sh python /cvar/jhlab/tp/DEPICT/src/python/depict.py /cvar/jhlab/tp/drop-seq/campbell-2016/src/depict_celltypes.cfg
