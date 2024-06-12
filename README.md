# Demo for compute canada

## Create environement

Clone this project

```
git clone git@github.com:arnaudjudge/demo_calculcan.git
```

### From login node run the following:

Load the python version you want
```
module load python/3.10
```

Create virtual env
```
virtualenv --no-download envdemocc
```

Activate your environment
```
source envdemocc/bin/activate
```

Update pip (recommended by ComputeCanada)
```
pip install --no-index --upgrade pip
```

Environment is created, go to project and install dependencies
```
cd demo_calculcan
pip install -r requirements.txt
```

# Setup

Download Cifar-10 (https://www.cs.toronto.edu/~kriz/cifar.html),copy to desired location. 
Easiest way is to download locally first, as CC restricts external connections.

Scratch can be useful for data and logs as it has a lot of space available. Keep in mind it is purged periodically.

Rename .env.example to .env and change default values if needed:
- Default data path in .env this folder must contain folder cifar-10-batches-py.
- Log path in .env
- Add comet api key if wanted, otherwise comet should simply log locally
  - If comet is not wanted, ```logger=False``` can be added as argument to main.py.

# Launch

Training can be launched in two different ways:

- Using sbatch and a launch script created manually:
  - ``` sbatch launch_cc.sh ```
  - Make sure to check all paths that are in the launch_cc script, to make sure datasets, etc. exist where they should, as these are hardcoded.
- With hydra configs through submitit:
  - ```python main.py launcher=<CLUSTER-NAME> --multirun```

# Tips

- Use tmux to avoid suspended terminals
- Look at resource usage and adjust requests accordingly for future tasks




