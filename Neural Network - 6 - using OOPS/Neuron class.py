import math
class Neuron:
    weights=list()      #list of weights
    gradw=list()        #gradient of all weights
    gradb=0             #gradient of b initialized weights
    bias=None
    delta=None          #computing the delta
    s=None              #total sum of the neuron
    a=None              #actual output of the neuron
    fprime=None         #output of the activation function
    inputs=list()       #list of inputs
    def computeSum(self,inputs):        #function to compute the sum
        self.sum=0
        for i in range(int(len(self.weights))):
            self.sum+=inputs[i]*self.weights[i]
        self.s=self.sum+self.bias
    def ComputeActivationFunctionDerivative(self):  #function to compute the activation function output
        self.fprime=self.a*(1-self.a)
        return self.fprime
    def Evaluate(self,inputs):                      #function to calculate the sum of the neuron
        self.computeSum(inputs)
        self.a=1/(1+math.exp(-1*self.s))
        x=self.ComputeActivationFunctionDerivative()
        return(self.a)
```
x=Neuron()
inputs=[1,2]
x.inputs=inputs
x.weights=[0.5,1.1]
x.bias=1
x.computeSum(inputs)
print(x.s)
```
