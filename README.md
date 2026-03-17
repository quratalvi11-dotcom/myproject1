# DataQuick 

[![PyPI version](https://badge.fury.io/py/dataquick.svg)](https://pypi.org/project/dataquick/)
[![Python](https://img.shields.io/pypi/pyversions/dataquick)](https://pypi.org/project/dataquick/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://img.shields.io/pypi/dm/dataquick)](https://pypi.org/project/dataquick/)

A fast and easy Auto EDA library for data scientists.

## Features
-  Auto data analysis
-  Missing values report
-  Data cleaning
-  Auto visualizations

## Installation
```bash
pip install dataquick
```

## Usage
```python
import pandas as pd
import dataquick as dq

df = pd.read_csv("data.csv")

dq.analyze(df)      # Full analysis
dq.clean(df)        # Auto clean
dq.visualize(df)    # Auto visualize
```

## Author
Made by [quratalvi11-dotcom](https://github.com/quratalvi11-dotcom)
