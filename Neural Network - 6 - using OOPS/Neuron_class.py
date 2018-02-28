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
        self.gradDescType=None
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
        m=len(self.input_x)
        n1=len(self.input_x[0])
        for k in range(NumEpochs):
            indata=list()
            for i in range(m):          #Record number
                for j in range(n1):     #Length / Number of inputs
                    indata.append(self.input_x[i][j])
                self.DoForwardPass(indata)
                indata.clear()
                output_num=0
            #Calculating Gradients for the last layer
                for n in (Layers[-1].Neurons):
                    n.delta=-1*(output_y[i][output_num]-n.a)*(n.fprime)
                    output_num+=1
                    temp_grad_list=[]
                    for g in range(len(n.weights)):
                        temp_grad_list.append(n.delta*Layers[-2].Neurons[g].a)
                    n.gradw=temp_grad_list[::]
                    n.gradb=n.delta
                    #print(n.gradw)
                    temp_grad_list.clear()

            #Compute deltas, grads on next layers, stop before input layer










            #Compute deltas, grads for the first layer
                neuron_num=0
                for n in (Layers[0].Neurons):       #selecting the neurons in the first layer
                    delta_sum=0                     #delta_sum because we accumulate the delta and weights of the next layer
                    temp_grad_list=[]
                    for k in range(len(Layers[1].Neurons)):
                        delta_sum+=Layers[1].Neurons[k].delta*Layers[1].Neurons[k].weights[neuron_num]
                    n.delta=delta_sum*n.fprime
                    for w in range(len(n.weights)):
                        t=n.delta*input_x[i][w]
                        temp_grad_list.append(t)
                    n.gradw=temp_grad_list[::]
                    n.gradb=n.delta
                    neuron_num+=1
                    temp_grad_list.clear()
                    #print(n.gradw)
                self.UpdateWeithtsAndBiases(0.01, 1)
                self.ClearGradients()
        for l in (Layers):
            for n in (l.Neurons):
                #print(n.weights)
                pass



    def UpdateWeithtsAndBiases(self,LearningRate,batch):
        for l in (Layers):
            for n in (l.Neurons):
                new_w=[]
                for i in range(len(n.weights)):
                    new_w.append(n.weights[i]-LearningRate*(n.gradw[i]/batch))
                n.weights.clear()
                n.weights=new_w[::]
                new_w.clear()
                n.bias=n.bias-LearningRate*(n.gradb/batch)
                #print(n.weights)

    def ClearGradients(self):
        for l in (Layers):
            for n in (l.Neurons):
                n.gradw.clear()
                n.gradb=None

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

        
NN.TrainByBackProp(10000,0.01)

#testing the Neural Network
for i in (input_x):
    x=NN.DoForwardPass(i)
    print("[0,1]"if x[0]<0.5 else "[1,0]")



