from main import *
import numpy as np 
import matplotlib.pyplot as plt

def run_mult(maxd,nest):
    trains = []
    tests = []
    for i in range(4):
        MLModel,train,test = Train_Model_yX_exp(TestSize=0.1,maxd=maxd,nest=nest)
        trains = trains + [train]
        tests = tests + [test]
    ts = np.mean(trains)
    ts2 = np.mean(tests)
    return (ts, ts2)

trains= []
tests = []
nests = [50]
for nest in nests:
    maxd = 6
    train,test = run_mult(maxd,nest)
    trains.append(train)
    tests.append(test)

plt.plot(nests,trains,'r--')
plt.plot(nests,tests,'b--')
plt.show()

