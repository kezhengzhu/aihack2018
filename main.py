import numpy as np
import pandas as pd


def db(*args):
    dbOn = True
    print(*args)


def load_data(filename):
    loaded_data = pd.read_csv('California/train/'+filename+'.csv')
    return loaded_data



def main():
    print("placeholder")

if __name__ == '__main__':
    main()