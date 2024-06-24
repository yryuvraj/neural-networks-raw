# neurons 
# raw python => then => numpy

# “What I cannot create, I do not understand” - Richard Feynman

import sys
import numpy as np

inputs = [1.2, 5.1, 2.1] #ouputs from the last layer, which are feeded in as inputs
weights = [3.1, 2.1, 8.7] #weights of the neurons
bias = 3 #bias of the neuron

output = (inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2]) + bias 
print(output)
