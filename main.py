import numpy as np
import pandas as pd
import os

def db(*args):
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
            db('B{} is not in the list of files available'.format(key))
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
    print("feature drop ratio : {} ".format(len(columns_missing_percentages)/len(df.columns)))
    new_df = df.drop(columns_missing_percentages,axis = 1)
    return(new_df)

def drop_rows(df):
    rows_missing_data_indexes_df = df.notnull().all(axis=1)
    new_df = df[rows_missing_data_indexes_df]
    print("raw drop ratio : {} ".format(1-(len(new_df)/len(df))))
    return new_df

def write_csv(filename,df):
    df.to_csv('California/train/'+filename+'.csv',index = False)

def drop_missing_values_and_save(filename,df,percentage):
    current_df = drop_columns(df,percentage)
    current_df = drop_rows(current_df)
    write_csv('dropped_'+filename,current_df)
    print('Done !')

def FormTrainingData():
    outputlist = ['B15002e3',
                     'B15002e4', 'B15002e5', 'B15002e6', 'B15002e7',
                     'B15002e8', 'B15002e9', 'B15002e10', 'B15002e11',
                     'B15002e12', 'B15002e13', 'B15002e14', 'B15002e15',
                     'B15002e16', 'B15002e17', 'B15002e18', 'B15002e20',
                     'B15002e21', 'B15002e22', 'B15002e23', 'B15002e24',
                     'B15002e25', 'B15002e26', 'B15002e27', 'B15002e28',
                     'B15002e29', 'B15002e30', 'B15002e31', 'B15002e32',
                     'B15002e33', 'B15002e34', 'B15002e35']

    df = get_data_by_key(outputlist)
    df.to_csv('TrainingData.csv', index=False)

def MergeonGeoID(x,y):
    dfx = pd.read_csv(x).set_index('GEOID')
    dfy = pd.read_csv(y).set_index('GEOID')
    center = dfy.join(dfx)
    center.to_csv('InputOutputMerged.csv')


def main():
    None

if __name__ == '__main__':
    MergeonGeoID('TrainingData.csv', 'OurInputs.csv')