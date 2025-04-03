import random

class Perceptron:
    def __init__(self, inputSize, learningRate=0.1, epochs=1000):
        self.weights = [random.random()] * inputSize
        print(self.weights)
        self.bias = 0.0
        self.learningRate = learningRate
        self.epochs = epochs

    def activation(self, x):
        return 1 if x >= 0.5 else 0

    def predict(self, inputs):
        
        wSum = 0
        for w, x in zip(self.weights, inputs):            
            wSum += w*x
        wSum += self.bias

        return self.activation(wSum)

    def train(self, training_data):
        for _ in range(self.epochs):
            for inputs, target in training_data:
     
                e = target - self.predict(inputs)
                # print(e)
                weights = []
                for w, x in zip(self.weights, inputs):
                    weights.append(w + self.learningRate * e * x)

                self.weights = weights

                self.bias += self.learningRate * e


trainingData = [
    # ([0, 0], 0),
    # ([0, 1], 0),
    # ([1, 0], 0),
    # ([1, 1], 1),
    ([1], 0),
    ([0], 1),  
]

perceptron = Perceptron(inputSize=1)

perceptron.train(trainingData)

# print(perceptron.predict([0, 0])) 
# print(perceptron.predict([1, 0])) 
# print(perceptron.predict([0, 1]))  
# print(perceptron.predict([1, 1])) 
print(perceptron.predict([1])) 
print(perceptron.predict([0])) 

