#!/bin/bash
#BSUB -J exercise_2_1
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=12GB]"
#BSUB -o exercise_2_1_%J.out
#BSUB -e exercise_2_1_%J.err

##BSUB -u s193992@student.dtu.dk
#BSUB -B 
#BSUB -N 

#BSUB -R "select[model == XeonGold6126 && avx512]"

#BSUB -R "span[hosts=1]"
#BSUB -n 1

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

for n in 256 512 1024; do
    python exercise_2_1.py $n
done