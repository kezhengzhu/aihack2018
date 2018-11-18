import main
import pandas as pd

a = main.CombineOutputGenders(pd.read_csv(r'california\train\Training_set_final.csv'))

a.to_csv('AggregatedOutputs.csv', index=False)