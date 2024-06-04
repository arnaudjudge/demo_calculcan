#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=12        # CPU cores/threads
#SBATCH --mem=32G               # memory per node
#SBATCH --time=0-06:00
nvidia-smi                        # you can use 'nvidia-smi' for a test

module load httpproxy # To allow connections to Comet server
#module load python/3.10 cuda cudnn

source ~/envdemocc/bin/activate

# move data
mkdir $SLURM_TMPDIR/data/

cp -r ~/scatch/data/cifar-10-python $SLURM_TMPDIR/data/
echo "data copied"

# train
python main.py

echo "done"