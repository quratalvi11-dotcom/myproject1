from dataquick.analyzer import DataAnalyzer
from dataquick.cleaner import DataCleaner
from dataquick.visualizer import DataVisualizer

def analyze(df):
    """Run full auto analysis on a DataFrame"""
    analyzer = DataAnalyzer(df)
    analyzer.analyze()

def clean(df, strategy="mean"):
    """Auto clean a DataFrame"""
    cleaner = DataCleaner(df)
    return cleaner.clean(strategy=strategy)

def visualize(df):
    """Auto visualize a DataFrame"""
    visualizer = DataVisualizer(df)
    visualizer.visualize()

__version__ = "0.1.0"
__author__ = "quratalvi11-dotcom"