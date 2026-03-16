# DataQuick 

A fast and easy Auto EDA library for data scientists.

## Features
- Auto data analysis
- Missing values report
- Data cleaning
- Auto visualizations

## Installation
```bash
pip install dataquick
```

## Usage
```python
import pandas as pd
from dataquick.analyzer import DataAnalyzer

df = pd.read_csv("data.csv")
analyzer = DataAnalyzer(df)
analyzer.analyze()
```