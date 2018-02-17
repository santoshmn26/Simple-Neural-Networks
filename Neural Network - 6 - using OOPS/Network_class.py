from Layer_class import *
class Network(Layer):
    Layers=list()
    input_x=list()
    output_y=list()
    def __init__(self,input_x,Layers,output_y):
        layer_num = 0
        self.Layers=Layers
        self.input_x=input_x
        self.output_y=output_y
        for i in range(len(Layers)):
            for j in (Layers[i].Neurons):
                temp = list()
                if(layer_num==0):
                    size_prev_input=input_x[0]
                else:
                    size_prev_input=Layers[i-1].Neurons
                for k in range(len(size_prev_input)):
                    rand_x = (random.uniform(0, 1))
                    rand_x = (float("{0:.2f}".format(rand_x)))
                    temp.append(rand_x)
                j.weights=temp[::]
                rb = (random.uniform(0, 1))
                rb = (float("{0:.2f}".format(rb)))
                j.bias = rb
            layer_num+=1
    def DoForwardPass(self,input_x):
        current_input = input_x
        for i in range(len(self.Layers)):
            next_input = list()
            for j in (Layers[i].Neurons):
                output=j.Evaluate(current_input)
                next_input.append(output)
            current_input=next_input[::]
        return(current_input)





    def TrainByBackProp(self,NumEpochs,LearningRate):
        for i in range(NumEpochs):
            error=0
            for j in range(len(self.input_x)):
                output=self.DoForwardPass(self.input_x[i])






l1=Layer(2)              #objects of layer class no neurons created yet
l2=Layer(2)              #objects of layer class no neurons created yet
Layers=list()
Layers.append(l1)
Layers.append(l2)
output_y=[[0,1],[1,0],[0,1],[1,0],[0,1],[1,0],[0,1],[1,0],[0,1],[1,0]]
input_x=[[1,2.2],[1,2.4],[2,2.5],[2,2.7],[3,2.8],[3,3],[4,3],[4,3.3],[5,3.4],[5,3.7]]
NN=Network(input_x,Layers,output_y)

for i in range(len(NN.Layers)):
    k=0
    for j in (NN.Layers[i].Neurons):
        print("Layer",i, "Neuron", k,"weights = ",j.weights, "bias = ",j.bias)
        k+=1
ff=NN.DoForwardPass(input_x[0])
print(ff)




'''
l=Layer()
l.layers(2)
for i in range(2):
    temp=list()
    for j in range(2):
        x = (random.uniform(0, 1))
        x = (float("{0:.2f}".format(x)))
        temp.append(x)
    l.Neurons[i].weights=temp[::]
    rb = (random.uniform(0, 1))
    rb = (float("{0:.2f}".format(rb)))
    l.Neurons[i].bias=rb
'''
