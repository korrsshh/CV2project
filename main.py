import numpy as np

def sigmoid(x):
    return 1 /(1+np.exp(-x))

training_inputs = np.array([[1,1,1],
                           [0,1,1],
                            [1,0,1],
                            [0,1,0],
                            ])
training_outputs = np.array([[1,0,0,0]]).T
np.random.seed(2)
synaptic_weights = 2*np.random.random((3,1))-1

print("Веса: ")
print(synaptic_weights)
for i in range(200000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer,synaptic_weights))
    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1-outputs)))
    synaptic_weights += adjustments
print('Результат: ')
print(outputs)

print('Случай 1:')

inputs1 = np.array([1,1,1])

outputs = sigmoid(np.dot(inputs1, synaptic_weights))
print('Результат: ')
print(outputs)
