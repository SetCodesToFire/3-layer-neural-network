import numpy as np

def nonlin(x,deriv-False):
    if(deriv=True):
        return x*(1-x)

    return 1/(1+np.exp(-x))

#input data
X = np.array([[0,0,1],
            [0,1,1],
            [1,0,1]
            [1,1,1]])

#output data
y = np.array([[0],
            [1],
            [1],
            [0]])

np.random.seed(1)

#synapses
syn0 = 2*np.random.random((3,4)) -1
syn1 = 2*np.random.random((4,1)) -1

#training step
for j in xrange
