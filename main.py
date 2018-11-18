import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
from sklearn import preprocessing

def db(*args):
    dbOn = True
    if dbOn:
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

def CombineOutputGenders(df):
    cols = 'B15002e{}-y'
    iterator = range(3, 19)
    friendly_name_dict = {3: 'No Schooling',
                          4: 'Up to 4th Grade',
                          5: '5-6th Grade',
                          6: '7-8th Grade',
                          7: '9th Grade',
                          8: '10th Grade',
                          9: '11th Grade',
                          10: '12th Grade - No Diploma',
                          11: 'High School Diploma',
                          12: '<1 Year of College',
                          13: 'Some College Education, No Degree',
                          14: 'Associates Degree',
                          15: 'Bachelors Degree',
                          16: 'Masters Degree',
                          17: 'Professional Degree',
                          18: 'PhD'}
    n = 0
    aggregated_outputs = pd.DataFrame()
    for i in iterator:
        aggregated_outputs[friendly_name_dict[i]] = df[cols.format(str(i))] + df[cols.format(str(i + 17))]
        n += 1
        aggregated_outputs['GEOID'] = df['GEOID']
    return aggregated_outputs


def MergeonGeoID(x,y):
    dfx = x.set_index('GEOID')
    dfy = y.set_index('GEOID')
    center = dfy.join(dfx)
    center.to_csv('NewMergedTrainingSet.csv')


def GetXy(filename ='Training_set_final',n_output = 32 ):
    Data =  np.copy(load_data(filename))[:,1:]
    n_features = Data.shape[1]
    X = Data[:,:n_features-32]
    y = Data[:,-32:]
    return X,y

def GetyX(filename ='NewMergedTrainingSet',n_output = 16 ):
    Data =  np.copy(load_data(filename))[:,1:]
    X = Data[:,n_output+1:]
    y = Data[:,1:n_output+1]
    print("X.shape : {} ".format(X.shape))
    print("y.shape : {} ".format(y.shape))
    return X,y

def Train_Model_yX(TestSize=0.05 ,filename ='NewMergedTrainingSet'):

    X,y = GetyX(filename)
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=TestSize)

    scaler_X = preprocessing.StandardScaler().fit(X_train)
    scaler_y = preprocessing.StandardScaler().fit(y_train)

    X_train_scaled = scaler_X.transform(X_train)
    y_train_scaled = scaler_y.transform(y_train)

    MLModel = RandomForestRegressor(n_estimators=200, random_state=0)
    MLModel.fit(X_train_scaled,y_train_scaled)

    X_test_scaled = scaler_X.transform(X_test)
    y_test_scaled = scaler_y.transform(y_test)

    print("Training Score : {} ".format(np.around(MLModel.score(X_train_scaled,y_train_scaled),decimals = 4)))
    print("Testing Score : {} \n".format(np.around(MLModel.score(X_test_scaled,y_test_scaled),decimals = 4)))

    return MLModel

def Train_Model(TestSize=0.05 ,filename ='Training_set_final'):

    X,y = GetXy(filename)
    X_train,X_test,y_train,y_test = train_test_split(X, y, test_size=TestSize)

    scaler_X = preprocessing.StandardScaler().fit(X_train)
    scaler_y = preprocessing.StandardScaler().fit(y_train)

    X_train_scaled = scaler_X.transform(X_train)
    y_train_scaled = scaler_y.transform(y_train)

    MLModel = RandomForestRegressor(n_estimators=200,n_jobs=-1, random_state=0)
    MLModel.fit(X_train_scaled,y_train_scaled)


    X_test_scaled = scaler_X.transform(X_test)
    y_test_scaled = scaler_y.transform(y_test)

    print("Training Score : {} ".format(np.around(MLModel.score(X_train_scaled,y_train_scaled),decimals = 4)))
    print("Testing Score : {} \n".format(np.around(MLModel.score(X_test_scaled,y_test_scaled),decimals = 4)))

    return MLModel

