import math
class Neuron:
    weights=list()
    gradw=list()
    gradb=0
    bias=None
    delta=None
    s=None
    a=None
    fprime=None
    inputs=list()
    def __init__(self):
        pass
    def computeSum(self,inputs):                    # This gives the sum
        self.sum=0
        for i in range(int(len(self.weights))):
            self.sum+=inputs[i]*self.weights[i]
        self.s=self.sum+self.bias


    def ComputeActivationFunctionDerivative(self):        #This is the activation function
        #self.fprime=self.a*(1-self.a)
        self.fprime = 1
        return self.fprime

    def Evaluate(self,inputs):                      # Actual output of the Neuron
        self.computeSum(inputs)
        self.a=1*self.s
        #self.a=1/(1+math.exp(-1*self.s))
        self.ComputeActivationFunctionDerivative()
        return(self.a)
