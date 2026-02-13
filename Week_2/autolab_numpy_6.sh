#!/bin/bash
#BSUB -J Matrix_Power_Job
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o Matrix_Power_Job_%J.out
#BSUB -e Matrix_Power_Job_%J.err

#BSUB -u s193992@student.dtu.dk
#BSUB -B 
#BSUB -N 

#BSUB -R "span[hosts=1]"
#BSUB -n 1

# Initialize the course conda environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Run the Python program
python autolab_numpy_5.py ./input.npy 10