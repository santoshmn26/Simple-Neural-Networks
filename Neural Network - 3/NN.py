import math
x0=int(input("Enter the value for x0: "))   #input for the x0
x1=int(input("Enter the value for x1: "))   #input for the x1
x=list()                                    #A list to store all the inputs
x.append(x0)
x.append(x1)
h0,h1,=list(),list()                        #list to store the input values of the hidden layer
H0,H1=list(),list()                         #list to store the hidden layer values
o0,o1=list(),list()                         #list to store the inputs for the activation function
O0,O1=list(),list()                         #list to store the results of the activation function
for i in range(2):
    t=float(input("Enter the weights for h0: "))        #get input for the activation function h0
    h0.append(t)
for j in range(2):
    t=float(input("Enter the weights for h1: "))        #get input for the activation function h0
    h1.append(t)
for k in range(2):
    t=float(input("Enter the weights for o0: "))        #get input for the output function o0
    o0.append(t)
for l in range(2):
    t=float(input("Enter the weights for o1: "))        #get input for the output function o1
    o1.append(t)
# Select Which activation function to be used
function=input("Select a value\n1. Linear Activation Function\n2. LeRU Activation Function ")
if(function==1):
    print("Activation function selected = Linear")
else:
    print("Activation function selected = ReLU")
# main logic to calculate the activation function results
for i in range(2):
    t = x[i] * h0[i]
    H0.append(t)
for i in range(2):
    t = x[i] * h1[i]
    H1.append(t)
h = list()  # Storing the results of the activation function
print(sum(H0),sum(H1))
if(function==2):
    if(sum(H0)>0):
        h.append(sum(H0))
    else:
        h.append(0)
    if(sum(H1)>0):
        h.append(sum(H1))
    else:
        h.append(0)
else:
    h.append(sum(H0))
    h.append(sum(H1))
for i in range(2):
    t = h[i] * o0[i]
    O0.append(t)
for i in range(2):
    t = h[i] * o1[i]
    O1.append(t)
print(round(sum(O0), 3), round(sum(O1), 3))
