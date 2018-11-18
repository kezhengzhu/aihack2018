from main import *
from get_short_list import *

def get_test_data_by_key(keylist,testdir):
    if (type(keylist) != list):
        raise Exception('get_test_data_by_key input is not a list of keys')
    numkeys = []
    for item in keylist:
        if item[1:3] not in numkeys:
            numkeys += [item[1:3]]
    files = get_alldir(testdir)
    file = dict()
    for key in numkeys:
        if key not in files:
            db('B{} is not in the list of files available'.format(key))
        else:
            file[key] = files[key]
    ldf = dict()
    for key in file:
        ldf[key] = pd.read_csv(file[key])

    fout = pd.read_csv(testdir+'/X00_COUNTS.csv')['GEOID']
    fout = fout.to_frame()
    for i in range(len(keylist)):
        k = keylist[i][1:3]
        if k in ldf:
            fout[keylist[i]] = ldf[k][keylist[i]]
    return fout

testdf = get_test_data_by_key(get_list(), 'test23/test23')
testInputs = combine_inputs(testdf)