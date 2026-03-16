import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class DataVisualizer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        self.df = df

    def plot_histograms(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        if len(numeric_cols) == 0:
            print("No numeric columns found for histogram!")
            return
        print("Plotting Histograms...")
        self.df[numeric_cols].hist(
            figsize=(15, 10),
            bins=20,
            color="steelblue",
            edgecolor="black"
        )
        plt.suptitle("Histograms of Numeric Columns", fontsize=16)
        plt.tight_layout()
        plt.show()

    def plot_correlation(self):
        numeric_cols = self.df.select_dtypes(include=np.number)
        if numeric_cols.empty:
            print("No numeric columns found for correlation!")
            return
        print("Plotting Correlation Heatmap...")
        plt.figure(figsize=(12, 8))
        sns.heatmap(
            numeric_cols.corr(),
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            linewidths=0.5
        )
        plt.title("Correlation Heatmap", fontsize=16)
        plt.tight_layout()
        plt.show()

    def plot_missing(self):
        missing = self.df.isnull().sum()
        missing = missing[missing > 0]
        if missing.empty:
            print("No missing values to plot!")
            return
        print("Plotting Missing Values...")
        plt.figure(figsize=(10, 6))
        sns.barplot(x=missing.index, y=missing.values, color="tomato")
        plt.title("Missing Values Per Column", fontsize=16)
        plt.xlabel("Columns")
        plt.ylabel("Missing Count")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def plot_boxplots(self):
        numeric_cols = self.df.select_dtypes(include=np.number).columns
        if len(numeric_cols) == 0:
            print("No numeric columns found for boxplot!")
            return
        print("Plotting Boxplots...")
        plt.figure(figsize=(15, 8))
        self.df[numeric_cols].plot(
            kind="box",
            figsize=(15, 8),
            patch_artist=True
        )
        plt.title("Boxplots for Outlier Detection", fontsize=16)
        plt.tight_layout()
        plt.show()

    def visualize(self):
        print("=" * 50)
        print("AUTO VISUALIZATION STARTED")
        print("=" * 50)
        self.plot_histograms()
        self.plot_correlation()
        self.plot_missing()
        self.plot_boxplots()
        print("=" * 50)
        print("Visualization Complete!")