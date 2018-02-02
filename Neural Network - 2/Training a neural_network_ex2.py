w1,w2,b=0.2,0.1,0.5 # initilize  the weights and Bias
x1=[1,1,2,2,3,3,4,4,5,5]        # Train data for x1
x2=[2.2,2.4,2.5,2.7,2.8,3,3,3.3,3.4,3.7]    # Train data for x2
y=[0,1,0,1,0,1,0,1,0,1,0]       # Train data output
tx1=[1.5,1.5,2.5,2.5]           # test data x1
tx2=[2.4,2.5,2.7,2.8]           # test data x2
def update_w1(x1,x2,w1,w2,b,y,a):   # update the weight for w1
    gradw1=-1*(y-a)*x1
    w=w1-(0.01*gradw1)
    return w
def update_w2(x1,x2,w1,w2,b,y,a):    # update the weight for w2
    gradw2=-1*(y-a)*x2
    w=w2-(0.01*gradw2)
    return w
def update_b(x1,x2,w1,w2,b,y,a):      # update the weight for b
    gradb=(-1 * (y - a))
    b1 = b-(0.01*gradb)
    return b1
for i in range(1000):               #Epcoh
    for i in range(10):
        a = (x1[i] * w1) + (x2[i] * w2) + b     # calculating the actual output
        new_w1=update_w1(x1[i], x2[i], w1, w2, b, y[i],a)   
        new_w2=update_w2(x1[i], x2[i], w1, w2, b, y[i],a)
        new_b=update_b(x1[i], x2[i], w1, w2, b, y[i],a)
        w1=new_w1
        w2=new_w2
        b=new_b
print(w1,w2,b)
while(True):        # Infinite loop to check the Neural network
    c=float(input())   # input x1
    d=float(input())   # input x2
    a1 = c * w1 + d* w2 + b
    print(a1)       # trained output

