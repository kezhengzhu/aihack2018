import numpy as np
import pandas as pd
import os

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

def get_alldir(path):
    '''Get all the files in data bank and put in dictionary, with key as '01','02' etc
    and file path as value '''
    result = os.listdir(path)
    dictfiles = dict()
    for i in range(len(result)):
        key = result[i][1:3]
        result[i] = path+'/'+result[i]
        dictfiles[key]=result[i]
    return dictfiles

def get_data_by_key(keylist):
    if (type(keylist) != list):
        raise Exception('get_data_by_key input is not a list of keys')
    numkeys = []
    for item in keylist:
        if item[1:3] not in numkeys:
            numkeys += [item[1:3]]
    files = get_alldir('california/train')
    file = dict()
    for key in numkeys:
        if key not in files:
            db('B{} is not in the list of files available'.format(numkey))
        else:
            file[key] = files[key]
    ldf = dict()
    for key in file:
        ldf[key] = pd.read_csv(file[key])

    fout = pd.read_csv('california/train/X00_COUNTS.csv')['GEOID']
    fout = fout.to_frame()
    for i in range(len(keylist)):
        k = keylist[i][1:3]
        if k in ldf:
            fout[keylist[i]] = ldf[k][keylist[i]]
    return fout

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