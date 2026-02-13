#!/bin/bash
#BSUB -J Hello_World
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o Hello_world_%J.out
#BSUB -e Hello_world_%J.err

##BSUB -u s193992@student.dtu.dk
#BSUB -B 
#BSUB -N 

#BSUB -R "select[model == XeonGold6126]"
#BSUB -R "select[avx512]"

/bin/sleep 60