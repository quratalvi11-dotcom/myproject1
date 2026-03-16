import pandas as pd
import numpy as np

class DataAnalyzer:
    def __init__(self, df):
        if not isinstance(df, pd.DataFrame):
            raise ValueError("Input must be a pandas DataFrame")
        self.df = df

    def basic_info(self):
        print("=" * 50)
        print("BASIC DATASET INFO")
        print("=" * 50)
        print(f"Shape        : {self.df.shape[0]} rows, {self.df.shape[1]} columns")
        print(f"Total Cells  : {self.df.size}")
        print(f"\nColumn Names : {list(self.df.columns)}")
        print(f"\nData Types:")
        print(self.df.dtypes)
        print("=" * 50)

    def missing_values(self):
        print("\n" + "=" * 50)
        print(" MISSING VALUES REPORT")
        print("=" * 50)
        missing = self.df.isnull().sum()
        percent = (missing / len(self.df)) * 100
        report = pd.DataFrame({
            "Missing Count": missing,
            "Missing %": percent.round(2)
        })
        report = report[report["Missing Count"] > 0]
        if report.empty:
            print(" No missing values found!")
        else:
            print(report)
        print("=" * 50)

    def duplicates(self):
        print("\n" + "=" * 50)
        print(" DUPLICATE ROWS REPORT")
        print("=" * 50)
        dup_count = self.df.duplicated().sum()
        print(f"Duplicate Rows: {dup_count}")
        if dup_count > 0:
            print("  Consider removing duplicates!")
        else:
            print(" No duplicate rows found!")
        print("=" * 50)

    def statistics(self):
        print("\n" + "=" * 50)
        print("STATISTICAL SUMMARY")
        print("=" * 50)
        print(self.df.describe())
        print("=" * 50)

    def analyze(self):
        self.basic_info()
        self.missing_values()
        self.duplicates()
        self.statistics()
        print("\n Analysis Complete!")