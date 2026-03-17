from .analyzer import DataAnalyzer
from .cleaner import DataCleaner
from .visualizer import DataVisualizer

def analyze(df):
    analyzer = DataAnalyzer(df)
    analyzer.analyze()

def clean(df, strategy="mean"):
    cleaner = DataCleaner(df)
    return cleaner.clean(strategy=strategy)

def visualize(df):
    visualizer = DataVisualizer(df)
    visualizer.visualize()

__version__ = "0.1.1"
__author__ = "quratalvi11-dotcom"
