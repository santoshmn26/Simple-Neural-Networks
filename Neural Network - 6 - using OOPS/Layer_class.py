from Neuron_class import *
class Layer(Neuron):
    Neurons=list()
    def layers(self,numNeurons):
        for i in range(numNeurons):
            n=Neuron()
            self.Neurons.append(n)
