from main import *
import pandas as pd 

MLModel = Train_Model_yX_exp(TestSize=0, nest=250)

testset = pd.read_csv('test23/test23/InputsNew.csv')

path = 'test23/test23/InputsNew.csv'
x,y = GetyX(n_output=0)

prediction = MLModel.predict(x)

print(prediction)