Creating a 2 layered neural network for the expression 
y=0.3x+2
Goal of the neural network is to classifiy the given points (x1,x2) into two classes either class 1 or class 0
if the given points lie below the line y=0.3x+2 then the output belongs to class 0 else the output belongs to class 1
-----------------------------------------------------------------------------------------------------------------------------------------
Information about the Neural Network
1. Number of Neurons - 4
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
    Epoch=10000
8. Error 
    E=1\2[{y1-a1_2}+{y2-a2_2}]
-----------------------------------------------------------------------------------------------------------------------------------------
Calculating weights
    1.  w11_2=-(y1-a1_2)*a1_1
    2.  w21_2=-(y2-a2_2)*a1_1
    3.  w12_2=-(y1-a1_2)*a2_1
    4.  w22_2=-(y2-a2_2)*a2_1
    5.  w11_1=-x1*1[(y1-a1_2)*1*w11_2+(y2-a2_2)*1*w21_2]
    6.  w12_1=-x2*1[(y1-a1_2)*1*w11_2+(y2-a2_2)*1*w21_2]
    7.  w21_1=-x1*1[(y1-a1_2)*1*w12_2+(y2-a2_2)*1*w22_2]
    8.  w22_1=-x2*1[(y1-a1_2)*1*w12_2+(y2-a2_2)*1*w22_2]

Calculating Bias
    1.  b1_1=-[(y1-a1_2)*1*w11_2+(y2-a2_2)*1*w21_2]
    2.  b2_1=-[(y1-a1_2)*1*w12_2+(y2-a2_2)*1*w22_2]
    3.  b1_2=-(y1-a1_2)
    4.  b2_2=-(y2-a2_2)
    
Calculating Delta's
        1. delta1_2=-1*(y1[i]-a1_2)
        2. delta2_2=-1*(y2[i]-a2_2)
        3. delta1_1=-1*((y1[i]-a1_2)*w11_2+(y2[i]-a2_2)*w21_2)
        4. delta2_1=-1*((y1[i]-a1_2)*w12_2+(y2[i]-a2_2)*w22_2)
