from Neuron_class import *                  #import the neuron class
class Layer(Neuron):                        #use the Neuron class as the parent class
    Neurons=list()                          #list to store the Neuron objects
    def layers(self,numNeurons):            #Create a list of Neurons
        for i in range(numNeurons):
            n=Neuron()                      
            self.Neurons.append(n)          #Storing the Neurons object in the list of Neurons
    
