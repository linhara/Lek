#2(?) layer nn

import numpy as np
import time

#variables
n_hidden = 10
n_in = 10
#outputs
n_out = 10
#sample data = 300
n_sample=300


#hyperparameters
learning_rate = 0.01
momentum = 0.9

np.random.seed(0)

def sigmoid(x):
    return 1.0/(1.0 + np.exp(-x))

def tanh_prime(x):
    return 1 - np.tanh(x)**2

#input data, transpose, layer1, layer2, biases
def train(x ,t, v, w, bv, bw):
    A = np.dot(x, v) + bv
    Z = np.tanh(A)

    B = np.dot(Z, w) + bw
    Y = sigmoid(B)

    Ew = Y - t
    Ev = tanh_prime(A) * np.dot(w, Ew)

    #predict our loss

    dW = np.outer(Z, Ew)
    dV = np.outer(x, Ev)

    #cross entrophy
    loss = -np.mean(t * np.log(Y) + (1 - t) * np.log(1-Y))

    return loss, (dV, dW, Ev, Ew)

def predict(x, v, w, bv, bw):
    A = np.dot(x, v) + bv
    B = np.dot(np.tanh(A), w) + bw
    xdd=((sigmoid(B)) > 0.5).astype(int)

    return (xdd) #ooof^2

#create layers
V = np.random.normal(scale=0.1, size=(n_in, n_hidden))
W = np.random.normal(scale=0.1, size=(n_hidden, n_out))

bv = np.zeros(n_hidden)
bw = np.zeros(n_out)

params = [V, W, bv, bw]

#generate our data
X = np.random.binomial(1, 0.5, (n_sample, n_in))
T = X ^ 1

#TRAINING TIME
for epoch in range(100):
    err = []
    upd = [0] * len(params)

    t0 = time.clock()
    #for each data point, update our weights
    for i in range(X.shape[0]):
        loss,grad = train(X[i], T[i], *params)
        #update loss
        for j in range(len(params)):
            params[j] -= upd[j]

        for j in range(len(params)):
            upd[j] =  learning_rate * grad[j] + momentum * upd[j]

        err.append(loss)

    print('epoch: %d, loss: %.8f, time: %.4fs' %(epoch, np.mean(err), time.clock()-t0))


X = np.random.binomial(1, 0.5, n_in)
print('XOR prediction')
print(X)
print(predict(X, *params))
