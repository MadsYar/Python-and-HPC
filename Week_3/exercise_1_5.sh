#!/bin/bash
#BSUB -J exercise_1_5
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=8GB]"
#BSUB -o exercise_1_5_%J.out
#BSUB -e exercise_1_5_%J.err

##BSUB -u s193992@student.dtu.dk
#BSUB -B 
#BSUB -N 

#BSUB -R "select[model == XeonGold6126 && avx512]"

#BSUB -R "span[hosts=1]"
#BSUB -n 1

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python exercise_1_5.py