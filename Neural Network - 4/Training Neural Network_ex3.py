w1,w2,w3,w4,b1,b2=0.2,-0.2,0.5,0.1,-0.6,0.25         # initialize the weights and bias
x1=[1,1,2,2,3,3,4,4,5,5]                             # training data sets
x2=[2.2,2.4,2.5,2.7,2.8,3,3,3.3,3.4,3.7]
y1=[0,1,0,1,0,1,0,1,0,1,0]
y2=[1,0,1,0,1,0,1,0,1,0,1]
def update_w(a,y,x,w):                   #updating the weights using back propagation
    gradw=(-1*(y-a)*x)
    n_w=w-0.01*gradw
    return n_w                           #updating the bias using back propagation
def update_b(a,y,b):
    gradb=(-1*(y-a))
    n_b=b-0.01*gradb
    return n_b
for j in range(1000):               #Epoch
    for i in range(10):
        a1=(x1[i]*w1)+(x2[i]*w2)+(1*b1)
        a2=(x1[i]*w3)+(x2[i]*w4)+(1*b2)
        new_w1=update_w(a1,y1[i],x1[i],w1)
        new_w2=update_w(a1,y1[i],x2[i],w2)
        new_w3=update_w(a2,y2[i],x1[i],w3)
        new_w4=update_w(a2,y2[i],x2[i],w4)
        new_b1=update_b(a1,y1[i],b1)
        new_b2=update_b(a2,y2[i],b2)
        w1,w2,w3,w4,b1,b2=new_w1,new_w2,new_w3,new_w4,new_b1,new_b2
print(w1,w2,w3,w4,b1,b2)
for i in range(10):             #checking the Neural Network
    y1 = x1[i] * w1 + x2[i]* w2 + b1
    y2= x1[i] * w3 + x2[i]* w4 + b2
    print(1 if y1>0.5 else 0,1 if y2>0.5 else 0)


