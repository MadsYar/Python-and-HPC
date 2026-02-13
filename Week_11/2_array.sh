#!/bin/bash
#BSUB -J name[2,29,71,73,127]
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -o name_%J.out
#BSUB -e name_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python preprocess.py input001.png