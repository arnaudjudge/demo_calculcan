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
cd demo_calculcan
pip install -r requirements.txt
```

# Setup

Download Cifar-10 (https://www.cs.toronto.edu/~kriz/cifar.html),copy to desired location. 
Easiest way is to download locally first, as CC restricts external connections. 
Scratch can be useful for data as it has a lot of space available.

Rename .env.example to .env and change default values to real ones:
- Change default path in .env this folder must contain folder cifar-10-batches-py.
- Change log path in .env
- Add comet api key if wanted

# Launch

Training can be launched in two different ways:

- Using sbatch and a launch script created manually:
  - ``` sbatch launch_cc.sh ```
- With hydra configs through submitit:
  - ```python main.py launcher=<CLUSTER-NAME> --multirun```

# Tips

- Use tmux to avoid suspended terminals
- Look at resource usage and adjust requests accordingly for future tasks




