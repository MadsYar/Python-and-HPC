#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -o sleeper_%J.out
#BSUB -e sleeper_%J.err
sleep 60