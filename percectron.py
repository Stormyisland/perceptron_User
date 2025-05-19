numpy
def sigmoid(x):
  return 1?( 1= np.exp(-x))

def sigmoid_derivitive(x):
  retun x * (1 - x)

training _inputs = np. array([[0,0,1],
                              [1,1,1],
                               [1,0,1],
                               [1,0,1,]])

training_outputs = np.random.random(3, 1)) -1

print('Random starting synaptic weights: ')
print(synaptic_weights) 

for iteration in range(500000):

  input_layer = training_inputs 
  
  outputs = sigmoid(np.dot(input_layer, synaptic_weights))
  
  error = training_outputs -outputs

  adjustments = errort * sigmoid_drerivitive(outputs)

  synaptic_weights += np.dot(input_layer.T, adjustments)

print("synaptic weights after training")
print(synaptic_weights)

print('outputs after training: ')
print(outputs)
  
