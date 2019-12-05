import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_der(x):
    return x * (1 - x)


training_inputs = np.array([[0, 0, 1, 1],
                            [1, 1, 1, 1],
                            [1, 0, 1, 1],
                            [0, 1, 1, 1]])

adjustmentmatr = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])


wantedtr_outputs = np.array([[0, 1, 1, 0]]).T
#test_inputs = np.array([[1, 0, 0]])

np.random.seed(1)
synaptic_weights = 9 * np.random.random((4, 1)) #- 1

print('Random starting synaptic weights: ')
print(synaptic_weights)


for iteration in range(50000):

    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    error = (wantedtr_outputs - outputs)
    adjustments = error #* sigmoid_der(outputs)
    synaptic_weights += np.dot(training_inputs.T, adjustments)

print("synaptic weights after training")
print(synaptic_weights)

print('Outputs after training: ')
print(outputs)

#resultat = sigmoid(np.dot(test_inputs, synaptic_weights))
#print(resultat)


