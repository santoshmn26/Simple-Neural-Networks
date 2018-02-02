Creating a 2 layered neural network for the expression 
y=0.3x+2
Goal of the neural network is to classifiy the given points (x1,x2) into two classes either class 1 or class 0
if the given points lie below the line y=0.3x+2 then the output belongs to class 0 else the output belongs to class 1
-----------------------------------------------------------------------------------------------------------------------------------------
Information about the Neural Network
1. Number of Neurons - 2
2. Activation Function - Linear 
    y=x
3. Number of Inputs - 2
    x1,x2
4. Number of outputs - 2
     y1,y2
5. Algorithm used for training the Neural Network
    Back Propagation
6. Learning Rate 
    LR=0.01
7. Number of Epoch
    Epoch=1000
-----------------------------------------------------------------------------------------------------------------------------------------
Calculating weights
    1. w1=-(y1-a1)*x1
    2. w2=-(y1-a1)*x2
    3. w3=-(y2-a2)*x1
    4. w4=-(y2-a2)*x2
Calculating Bias
    1. b1=-(y1-a1)
    2. b2=-(y2-a2)
    
