w=0.1  # initilize random values for weights and bias
b=0.4
x=0
def update_w(x,w,b): #update the new weight value using back propagation
    a=w*x+b          #actual obtained value
    y=0.3*x+2        #Expected value
    gradw=-1*(y-a)*x #Gradient value
    w=w-0.01*gradw   #Back propagation formula
    return w
def update_b(x,w,b): #Update the new bias value using back propagation
    a = w * x + b    #Actual obtained value
    y = 0.3 * x + 2  #Expected value
    gradb = -1 * (y - a) * 1  #Gradient Value
    b = b - 0.01 * gradb  #Back propagation formula
    return b
for j in range(1000):  # Training the Neural Network, Total of 1000 epoch
    for i in range(1,11):   # Training the same data set for 1 to 10
        x=i
        new_w=update_w(x,w,b)
        new_b=update_b(x,w,b)
        w=new_w         # Updating the new values of the weights
        b=new_b         # Updating the new values of the bias
print(w,b)
for i in range(1,10):
    r=i*w+1*b           # Testing data verifying the neural Network
    print(r)