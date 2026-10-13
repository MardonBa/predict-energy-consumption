# predict-energy-consumption

Time series regression with XGBoost on the [PJM hourly energy consumption dataset](https://www.kaggle.com/datasets/robikscube/hourly-energy-consumption).

The goal is to build the whole pipeline end to end, by hand, and learn each piece along the way. The final writeup
(maybe a blog post) will cover what I learned, experiment results, where the error comes from, how to interpret the model,
and how the experiments were designed.

## Pipeline

1. Time series preprocessing
2. Feature engineering
3. Temporal train/val/test splits
4. Baselines and tuning
5. XGBoost regression
6. Avoiding time series leakage
7. Error analysis
8. Model interpretability
9. Reproducible experiments

## Status

Not started yet. See [WORK_LOG.md](WORK_LOG.md) for progress.
