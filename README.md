# Demo for compute canada

## Create environement

Clone this project

git clone git@github.com:arnaudjudge/demo_calculcan.git

### From login node run the following:

Load the python version you want

```module load python/3.10```

Create virtual env

```virtualenv --no-download envdemocc```

Activate your environment

```source envdemocc/bin/activate```

Update pip (recommended by ComputeCanada)

```pip install --no-index --upgrade pip```

Environment is created, go to project and install dependencies

```
cd demo_calulcan
pip install -r requirements.txt
```

# Setup

Download Cifar-10, extract to your desired data folder. Scratch can be useful for data as it has a lot of space available.




Change default path in .env this folder must contain folder cifar-10-batches-py.
Change log path in .env
Add comet api key to .env

# Launch

to run training:

sbatch launch_cc.sh

or with hydra configs through submitit:

python main.py +launcher=<CLUSTER-NAME> --multirun





