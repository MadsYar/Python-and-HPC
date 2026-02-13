#!/bin/bash
#BSUB -J matmul_job
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -n 8
#BSUB -R "span[hosts=1]"
#BSUB -R "select[model == XeonGold6126 && avx512]"
#BSUB -o matmul_%J.out
#BSUB -e matmul_%J.err

source /dtu/projects/02613_2024/conda/conda_init.sh
conda activate 02613

export OMP_NUM_THREADS=8  
export MKL_NUM_THREADS=8 
export MPI_NUM_THREADS=8 
export OPENBLAS_NUM_THREADS=8

python -u matmul.py