import main
import pandas as pd

x = pd.read_csv(r'california\train\NewInputs.csv')
y = pd.read_csv('AggregatedOutputs.csv')
main.MergeonGeoID(x, y)
