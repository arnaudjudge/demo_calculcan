# demo_calculcan
Demo for compute canada

From login node, after git clone of this repo

module load python/3.10
module load httpproxy

virtualenv --no-download envdemocc

source envdemocc/bin/activate

pip install --no-index --upgrade pip

cd demo_calulcan

pip install -r requirements.txt




