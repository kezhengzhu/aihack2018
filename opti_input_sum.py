from get_short_list import *

def combine_inputs2(df):
    dfout = df.iloc[:,0:7].copy()
    cols = list(df)

    print(len(cols))

    ageSum1 = cols[7:14]+cols[30:37]
    ageSum2 = cols[14:19]+cols[37:42] # Change age bracket to <21, 21-45, 45+
    ageSum3 = cols[19:30]+cols[42:53]
    dfout['AgeSum1'] = df[ageSum1].sum(axis=1)
    dfout['AgeSum2'] = df[ageSum2].sum(axis=1)
    dfout['AgeSum3'] = df[ageSum3].sum(axis=1)

    raceKeepList = [cols[53],cols[54],cols[56],cols[59]]
    dfout[raceKeepList] = df[raceKeepList]
    nextKeep = [cols[60],cols[62],cols[63],cols[65]]

    schEnrol1 = cols[66:74]
    schEnrol2 = cols[74:80]
    schEnrol3 = cols[80:82]
    publicSum = cols[82:96]
    privateSum = cols[96:110]

    dfout['SchEnrol1'] = df[schEnrol1].sum(axis=1)
    dfout['SchEnrol2'] = df[schEnrol2].sum(axis=1)
    dfout['SchEnrol3'] = df[schEnrol3].sum(axis=1)
    dfout['publicSum'] = df[publicSum].sum(axis=1)
    dfout['privateSum'] = df[privateSum].sum(axis=1)

    dfout[cols[110]] = df[cols[110]]

    limitedEng = cols[111:115]
    dfout['LimitedEng'] = df[limitedEng].sum(axis=1)

    dfout[cols[115]] = df[cols[115]]
    pov12 = cols[116:121]
    dfout['PovBtwn12'] = df[pov12].sum(axis=1)
    keepList = cols[121:122]
    dfout[keepList] = df[keepList]

    income25k = cols[123:127]
    income50k = cols[127:132]
    income100k = cols[132:135]
    income200k = cols[135:138]
    dfout['Income25k'] = df[income25k].sum(axis=1)
    dfout['Income50k'] = df[income50k].sum(axis=1)
    dfout['Income100k'] = df[income100k].sum(axis=1)
    dfout['Income200k'] = df[income200k].sum(axis=1)
    print(len(cols))
    keep = cols[138:141]
    dfout[keep] = df[keep]

    return dfout

def combine_inputs3(df):
    dfout = df.iloc[:,0:7].copy()
    cols = list(df)

    print(len(cols))

    ageSum1 = cols[7:15]+cols[30:38]
    ageSum2 = cols[15:25]+cols[38:48]
    ageSum3 = cols[25:30]+cols[48:53]
    dfout['AgeSum1'] = df[ageSum1].sum(axis=1)
    dfout['AgeSum2'] = df[ageSum2].sum(axis=1)
    dfout['AgeSum3'] = df[ageSum3].sum(axis=1)

    raceKeepList = [cols[53],cols[54],cols[56],cols[59]]
    dfout[raceKeepList] = df[raceKeepList]
    nextKeep = [cols[60],cols[62],cols[63],cols[65]]

    schEnrol1 = cols[66:74]
    schEnrol2 = cols[74:80]
    schEnrol3 = cols[80:82]
    publicSum = cols[82:96]
    privateSum = cols[96:110]

    dfout['SchEnrol1'] = df[schEnrol1].sum(axis=1)
    dfout['SchEnrol2'] = df[schEnrol2].sum(axis=1)
    dfout['SchEnrol3'] = df[schEnrol3].sum(axis=1)
    dfout['publicSum'] = df[publicSum].sum(axis=1)
    dfout['privateSum'] = df[privateSum].sum(axis=1)

    dfout[cols[110]] = df[cols[110]]

    limitedEng = cols[111:115]
    dfout['LimitedEng'] = df[limitedEng].sum(axis=1)

    dfout[cols[115]] = df[cols[115]]
    pov12 = cols[116:121]
    dfout['PovBtwn12'] = df[pov12].sum(axis=1)
    keepList = cols[121:122]
    dfout[keepList] = df[keepList]

    income25k = cols[123:126] # Income bracket changed to 20k, 60k, 150k, 150+
    income50k = cols[126:133]
    income100k = cols[133:137]
    income200k = cols[137:138]
    dfout['Income25k'] = df[income25k].sum(axis=1)
    dfout['Income50k'] = df[income50k].sum(axis=1)
    dfout['Income100k'] = df[income100k].sum(axis=1)
    dfout['Income200k'] = df[income200k].sum(axis=1)
    print(len(cols))
    keep = cols[138:141]
    dfout[keep] = df[keep]

    return dfout

def combine_inputs4(df):
    dfout = df.iloc[:,0:7].copy()
    cols = list(df)

    print(len(cols))

    ageSum1 = cols[7:15]+cols[30:38]
    ageSum2 = cols[15:25]+cols[38:48]
    ageSum3 = cols[25:30]+cols[48:53]
    dfout['AgeSum1'] = df[ageSum1].sum(axis=1)
    dfout['AgeSum2'] = df[ageSum2].sum(axis=1)
    dfout['AgeSum3'] = df[ageSum3].sum(axis=1)

    raceKeepList = [cols[53],cols[54],cols[56],cols[59]]
    dfout[raceKeepList] = df[raceKeepList]
    nextKeep = [cols[60],cols[62],cols[63],cols[65]]

    schEnrol1 = cols[66:74]
    schEnrol2 = cols[74:80]
    schEnrol3 = cols[80:82]
    publicSum = cols[82:96]
    privateSum = cols[96:110]

    dfout['SchEnrol1'] = df[schEnrol1].sum(axis=1)
    dfout['SchEnrol2'] = df[schEnrol2].sum(axis=1)
    dfout['SchEnrol3'] = df[schEnrol3].sum(axis=1)
    dfout['publicSum'] = df[publicSum].sum(axis=1)
    dfout['privateSum'] = df[privateSum].sum(axis=1)

    dfout[cols[110]] = df[cols[110]]

    limitedEng = cols[111:115]
    dfout['LimitedEng'] = df[limitedEng].sum(axis=1)

    dfout[cols[115]] = df[cols[115]] # Expand poverty to include 1-1.5,1.5-2
    pov115 = cols[116:119]
    pov152 = cols[119:121]
    dfout['PovBtwn1_1.5'] = df[pov115].sum(axis=1)
    dfout['PovBtwn1.5_2'] = df[pov152].sum(axis=1)
    keepList = cols[121:122]
    dfout[keepList] = df[keepList]

    income25k = cols[123:127]
    income50k = cols[127:132]
    income100k = cols[132:135]
    income200k = cols[135:138]
    dfout['Income25k'] = df[income25k].sum(axis=1)
    dfout['Income50k'] = df[income50k].sum(axis=1)
    dfout['Income100k'] = df[income100k].sum(axis=1)
    dfout['Income200k'] = df[income200k].sum(axis=1)
    print(len(cols))
    keep = cols[138:141]
    dfout[keep] = df[keep]

    return dfout

def combine_inputs5(df):
    dfout = df.iloc[:,0:7].copy()
    cols = list(df)

    print(len(cols))

    ageSum1 = cols[7:15]+cols[30:38]
    ageSum2 = cols[15:25]+cols[38:48]
    ageSum3 = cols[25:30]+cols[48:53]
    dfout['AgeSum1'] = df[ageSum1].sum(axis=1)
    dfout['AgeSum2'] = df[ageSum2].sum(axis=1)
    dfout['AgeSum3'] = df[ageSum3].sum(axis=1)

    raceKeepList = [cols[53],cols[54],cols[56],cols[59]]
    dfout[raceKeepList] = df[raceKeepList]
    nextKeep = [cols[60],cols[62],cols[63],cols[65]]

    schEnrol1 = cols[66:74]
    schEnrol2 = cols[74:80]
    schEnrol3 = cols[80:82]
    publicSum = cols[82:96]
    privateSum = cols[96:110]

    dfout['SchEnrol1'] = df[schEnrol1].sum(axis=1)
    dfout['SchEnrol2'] = df[schEnrol2].sum(axis=1)
    dfout['SchEnrol3'] = df[schEnrol3].sum(axis=1)
    dfout['publicSum'] = df[publicSum].sum(axis=1)
    dfout['privateSum'] = df[privateSum].sum(axis=1)

    dfout[cols[110]] = df[cols[110]]

    limitedEng = cols[111:115]
    dfout['LimitedEng'] = df[limitedEng].sum(axis=1)

    dfout[cols[115]] = df[cols[115]]
    pov12 = cols[116:121]
    dfout['PovBtwn12'] = df[pov12].sum(axis=1)
    keepList = cols[121:122]
    dfout[keepList] = df[keepList]

    income25k = cols[123:126] # reduce brackets to 20k, 100k, 100k+
    income50k = cols[127:135]
    income200k = cols[135:138]
    dfout['Income25k'] = df[income25k].sum(axis=1)
    dfout['Income50k'] = df[income50k].sum(axis=1)
    dfout['Income200k'] = df[income200k].sum(axis=1)
    print(len(cols))
    keep = cols[138:141]
    dfout[keep] = df[keep]

    return dfout

df = pd.read_csv('OurInputs.csv')
opti_set2 = combine_inputs2(df)
opti_set2.to_csv('OptiInputs2.csv', index=False)
opti_set3 = combine_inputs3(df)
opti_set3.to_csv('OptiInputs3.csv', index=False)
opti_set4 = combine_inputs4(df)
opti_set4.to_csv('OptiInputs4.csv', index=False)
opti_set5 = combine_inputs5(df)
opti_set5.to_csv('OptiInputs5.csv', index=False)
