## Creating a Neural Network using OOPS concepts:
### We will develop an implementation of the Backpropagation algorithm so that any number of inputs, outputs and hidden layers can be specified.
The project consists of 3 classes
```
  1. Neuron class
  2. Layer class
  3. Network class
```
### Information about the Neural Network
```
1. Number of Neurons - Can be specified during Run time
2. Activation Function - Sigmoid 
    y=1(1+e**(-x))
3. Number of Inputs - Can be specified during Run time
    x1,x2.....
4. Number of outputs - Can be specified during Run time
     y1,y2....
5. Algorithm used for training the Neural Network
    Back Propagation
6. Learning Rate 
    LR=0.01
7. Number of Epoch
    Epoch=10000   (Optional can be changed during execution time)
```
### Information about the files
```
  The Neural Network is coded with the help of OOP's concept and python 
  The Project consists of 3 class files
```
    1. Neuron Class (Level 1 Base Class)
    2. Layer Class (Level 2 - Inherited Neuron class)
    3. Network Class  (Level 3 - Inherited Layer class)
``` 
Neuron Class just maintaines a object of a single Neuron
Layer Class consists of a list of Neurons
Network Class consists of a list of Layer 

### Two files are used to train the NN which are the training data
```
  1. Input matrix (Input values)
  2. Output matrix  (Output Values)
```
### Limitation about this project
```
  1. Number of neurons in the first layer must be equal to Number of inputs
  2. Number of neurons in the last layer must be equal to Number of outputs
  3. Hidden layer can consists of any number of neurons
```
