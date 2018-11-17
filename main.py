import numpy as np
import pandas as pd


def db(*args):
    dbOn = True
    print(*args)


def load_data(filename):
    loaded_data = pd.read_csv('California/train/'+filename+'.csv')
    return loaded_data

def Full_name_parser():
    metadata = load_data('BG_METADATA_2016')
    List_of_names = []
    for line in metadata['Full_Name']:
        parsed_line = line.split(':')[0]
        if parsed_line not in List_of_names:
            List_of_names.append(parsed_line)
    return List_of_names

def drop_columns(df,percentage):
    columns_missing_percentages = []
    for column in df.columns:
        current_column = df[column]
        current_percentage_missing = (current_column.isna().sum())/len(current_column)
        if current_percentage_missing > percentage:
            columns_missing_percentages.append(column)
    new_df = df.drop(columns_missing_percentages,axis = 1)
    return(new_df)

def main():
    print("placeholder")

if __name__ == '__main__':
    main()