#!/bin/bash
#SBATCH --gpus-per-node=1
#SBATCH --cpus-per-task=12        # CPU cores/threads
#SBATCH --mem=32G                 # memory per node
#SBATCH --time=0-00:15            # 15 minutes
nvidia-smi                        # you can use 'nvidia-smi' for a test

module load httpproxy # To allow connections to Comet server

source ~/envdemocc/bin/activate

# move data
mkdir $SLURM_TMPDIR/data/

cp -r ~/demo_calculcan/ $SLURM_TMPDIR
echo "project copied"

cp -r ~/projects/def_pmjodoin/datasets/cifar10 $SLURM_TMPDIR/data/
echo "data copied"

cd $SLURM_TMPDIR/demo_calculcan/

# train
python main.py

echo "done"