# Map-Free DRL Navigation With Zero-Shot Sim-to-Real Transfer

Reproducibility repository for the IEEE Access article:

**A Comparative Study of DRL Algorithms for Map-Free Robot Navigation With Zero-Shot Sim-to-Real Transfer**

Taner Yilmaz and Omur Aydogmus, *IEEE Access*, vol. 14, pp. 60268-60284, 2026.

- DOI: [10.1109/ACCESS.2026.3684520](https://doi.org/10.1109/ACCESS.2026.3684520)
- IEEE Xplore: [Document 11482413](https://ieeexplore.ieee.org/document/11482413/)
- Web of Science UID: `WOS:001748497200045`
- ORCID: [Taner Yilmaz](https://orcid.org/0000-0002-1721-9071)
- License for article: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
- License for repository code: MIT

## Overview

This repository contains the training and evaluation pipeline used for comparing deep reinforcement learning algorithms in map-free mobile robot navigation. The work focuses on zero-shot sim-to-real transfer, where policies trained in simulation are evaluated for transfer to real-world robot navigation without additional real-world fine-tuning.

The repository provides:

- A custom Python simulator based on a Gymnasium environment.
- Episode-randomized static obstacles in a 10 m x 10 m arena.
- Training scripts for PPO, SAC, A2C, TD3, and DDPG with Stable-Baselines3.
- Optuna hyperparameter optimization scripts with a fixed-seed protocol.
- Evaluation scripts for success, collision, timeout, and path-length metrics.
- Documentation for ROS/Gazebo and TurtleBot3 Burger deployment.

## Repository Layout

The implementation is located in [`drl_nav_repro_repo/`](drl_nav_repro_repo/).

```text
drl_nav_repro_repo/
  configs/       Environment, reward, and hyperparameter settings
  docs/          Reproduction and ROS/Gazebo notes
  ros_gazebo/    ROS/Gazebo placeholders
  scripts/       Training, evaluation, Optuna, and helper scripts
  sim/           Custom simulator and LiDAR utilities
  tests/         Basic environment tests
```

## Quickstart

```bash
cd drl_nav_repro_repo
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/sanity_check_env.py --episodes 3
```

On Windows PowerShell:

```powershell
cd drl_nav_repro_repo
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python scripts\sanity_check_env.py --episodes 3
```

## Training

```bash
python scripts/train.py --algo PPO --episodes 100000 --seed 42 --cfg configs/best_hparams.yaml
```

Supported algorithms include `PPO`, `SAC`, `A2C`, `TD3`, and `DDPG`.

## Evaluation

```bash
python scripts/eval.py --algo PPO --model runs/PPO_seed42/model.zip --episodes 20 --seed 42 --deterministic
```

## Hyperparameter Tuning

```bash
python scripts/optuna_tune.py --algo PPO --trials 80 --steps-per-trial 300000 --seed 123 --search-space configs/optuna_search_space.yaml
```

## Reproducibility Protocol

- Arena: 10 m x 10 m, 4 walls.
- Obstacles: axis-aligned rectangles, randomized at the start of each episode and stationary within the episode.
- Control interval: delta t = 0.2 s.
- Max episode length: 1000 steps.
- Stage-1 feasibility screen: 10,000 episodes for all algorithms.
- Stage-2 retrain from scratch: 100,000 episodes for selected algorithms.
- Seed averaging: mean over 5 independent seeds.

See [`drl_nav_repro_repo/docs/REPRODUCE_PAPER.md`](drl_nav_repro_repo/docs/REPRODUCE_PAPER.md).

## Citation

If you use this repository, discuss the experiments, or build on the simulator, please cite:

```bibtex
@article{yilmaz2026comparative,
  author = {Yilmaz, Taner and Aydogmus, Omur},
  title = {A Comparative Study of DRL Algorithms for Map-Free Robot Navigation With Zero-Shot Sim-to-Real Transfer},
  journal = {IEEE Access},
  year = {2026},
  volume = {14},
  pages = {60268--60284},
  doi = {10.1109/ACCESS.2026.3684520},
  publisher = {IEEE}
}
```

## Keywords

Deep reinforcement learning, map-free navigation, mobile robot navigation, zero-shot sim-to-real transfer, autonomous robots, robot learning, Stable-Baselines3, ROS, Gazebo, TurtleBot3.
