import pandas as pd

def get_list():
    res = [ 'B00001e1', # Unweighted population [1]
            'B00002e1', # Unweighted no of households
            'B01001e1', # Total population
            'B11001e1', # Total no of households
            'B01001e2', # Male
            'B01001e26', # Female
            'B01001e3', # M age start <5 [7]
            'B01001e4', # 5-9
            'B01001e5', # 10-14
            'B01001e6', # 15-17
            'B01001e7', # 18-19
            'B01001e8', # 20
            'B01001e9', # 21
            'B01001e10', # 22-24 [14]
            'B01001e11', # 25-29 [15]
            'B01001e12', # 30-34
            'B01001e13', # 35-39
            'B01001e14', # 40-44
            'B01001e15', # 45-49
            'B01001e16', # 50-54
            'B01001e17', # 55-59
            'B01001e18', # 60-61
            'B01001e19', # 62-64
            'B01001e20', # 65-66 [24]
            'B01001e21', # 67-69 [25]
            'B01001e22', # 70-74
            'B01001e23', # 75-79
            'B01001e24', # 80-85
            'B01001e25', # M age end 85+ [29]
            'B01001e27', # F age start [30]
            'B01001e28', #
            'B01001e29', #
            'B01001e30', #
            'B01001e31', #
            'B01001e32', #
            'B01001e33', #
            'B01001e34', # [37]
            'B01001e35', # [38]
            'B01001e36', #
            'B01001e37', #
            'B01001e38', #
            'B01001e39', #
            'B01001e40', #
            'B01001e41', #
            'B01001e42', #
            'B01001e43', #
            'B01001e44', # [47]
            'B01001e45', # [48]
            'B01001e46', #
            'B01001e47', #
            'B01001e48', #
            'B01001e49', # F age end [52]
            'C02003e3', # Total white
            'C02003e4', # Total black
            'C02003e5', # Total native [55]
            'C02003e6', # Total asian
            'C02003e7', # Total hawaiian [57]
            'C02003e8', # Total others [58]
            'B03003e3', # Total Hispanic and Latinos
            'B11001e2', # Total Family households [60]
            'B11001e7', # Total non-family households
            'B11003e1', # Total families with children [62]
            'B11003e2', # Families w child married [63]
            'B11003e8', # Families w child not married
            'B14007e2', # Total school enrollment [65]
            'B14007e3', # Nusery enrollment [66]
            'B14007e4', # Kindergarten [67]
            'B14007e5', # Grade .. [68]
            'B14007e6', #
            'B14007e7', #
            'B14007e8', #
            'B14007e9', #
            'B14007e10', # Grade 6 [73]
            'B14007e11', # Grade 7 [74]
            'B14007e12', #
            'B14007e13', #
            'B14007e14', #
            'B14007e15', #
            'B14007e16', # Grade 12 [79]
            'B14007e17', # College [80]
            'B14007e18', # Grad or prof school
            'B14002e5', # Public: Male start [82]
            'B14002e8',
            'B14002e11',
            'B14002e14',
            'B14002e17',
            'B14002e20',
            'B14002e23', # Public: Male end [88]
            'B14002e29', # Private: Female start
            'B14002e32',
            'B14002e35',
            'B14002e38',
            'B14002e41',
            'B14002e44',
            'B14002e47', # Public: Female end [95]
            'B14002e6', # Private: Male start [96]
            'B14002e9',
            'B14002e12',
            'B14002e15',
            'B14002e18',
            'B14002e21',
            'B14002e24', # Private: Male end
            'B14002e30', # Private: Female start
            'B14002e33',
            'B14002e36',
            'B14002e39',
            'B14002e42',
            'B14002e45',
            'B14002e48', # Private: Female end [109]
            'C16002e2', # Language: English only household [110]
            'C16002e4', # Limited english start [111]
            'C16002e7', 
            'C16002e10', 
            'C16002e13', # Limited english end [114]
            'C17002e2', # Ratio income to pov <.50 [115]
            'C17002e3', # Ratio income to pov .50-.99 [116]
            'C17002e4', # Ratio income to pov 1.00-1.24 
            'C17002e5', # Ratio income to pov 1.25-1.49 
            'C17002e6', # Ratio income to pov 1.50-1.84
            'C17002e7', # Ratio income to pov 1.84-1.99
            'C17002e8', # Ratio income to pov >2.00 [121]
            'B17010e1', # Families with related children [122]
            'B19001e2', # Income brackets: <10k [123]
            'B19001e3', # Income brackets: 10k-15k
            'B19001e4', # Income brackets: 15-20k 
            'B19001e5', # Income brackets: 20k-25k [126]
            'B19001e6', # Income brackets: 25k-30k [127]
            'B19001e7', # Income brackets: 30-35
            'B19001e8', # Income brackets: 35-40
            'B19001e9', # Income brackets: 40-45
            'B19001e10', # Income brackets: 45-50 [131]
            'B19001e11', # Income brackets: 50-60 [132]
            'B19001e12', # Income brackets: 60-75
            'B19001e13', # Income brackets: 75-100  [134]
            'B19001e14', # Income brackets: 100-125 [135]
            'B19001e15', # Income brackets: 125-150 
            'B19001e16', # Income brackets: 150-200 [137]
            'B19001e17', # Income brackets: >200k [138]
            'B22010e1', # Food stamps [139]
            'B23025e2', # Employment status: In labor force [140]
            'B23025e7' # Employment status: Not in labor force
            ]
    return res 

def combine_inputs(df):
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

def main():
    df = pd.read_csv('OurInputs.csv')
    dfout = combine_inputs(df)
    dfout.to_csv('NewInputs.csv', index=False)

if __name__ == '__main__':
    main()