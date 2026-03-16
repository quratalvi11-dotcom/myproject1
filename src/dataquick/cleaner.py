import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        self.df = df.copy()

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        print(f"Removed {before - after} duplicate rows")
        return self

    def fill_missing(self, strategy="mean"):
        """
        strategy: 'mean', 'median', 'mode', 'drop'
        """
        if strategy == "drop":
            before = len(self.df)
            self.df = self.df.dropna()
            print(f"Dropped {before - len(self.df)} rows with missing values")

        elif strategy == "mean":
            numeric_cols = self.df.select_dtypes(include=np.number).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].mean())
            print("Filled missing values with mean")

        elif strategy == "median":
            numeric_cols = self.df.select_dtypes(include=np.number).columns
            self.df[numeric_cols] = self.df[numeric_cols].fillna(self.df[numeric_cols].median())
            print("Filled missing values with median")

        elif strategy == "mode":
            for col in self.df.columns:
                self.df[col] = self.df[col].fillna(self.df[col].mode()[0])
            print("Filled missing values with mode")

        return self

    def fix_dtypes(self):
        for col in self.df.columns:
            try:
                self.df[col] = pd.to_numeric(self.df[col])
            except:
                pass
        print("Fixed data types where possible")
        return self

    def clean(self, strategy="mean"):
        print("=" * 50)
        print("AUTO CLEANING STARTED")
        print("=" * 50)
        self.remove_duplicates()
        self.fill_missing(strategy=strategy)
        self.fix_dtypes()
        print("=" * 50)
        print("Cleaning Complete!")
        return self.df