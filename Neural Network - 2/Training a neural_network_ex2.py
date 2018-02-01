w1,w2,b=0.2,0.1,0.5
x1=[0.5,0.5,1,1,1.5,1.5,2,2,2.5,2.5]
x2=[2,2.4,2.4,2.5,2.4,2.6,2.5,2.7,2.6,2.8]
y=[0,1,0,1,0,1,0,1,0,1]
tx1=[1.5,1.5,2.5,2.5]
tx2=[2.4,2.5,2.7,2.8]
def update_w1(x1,x2,w1,w2,b,y):
    a=x1*w1+x2*w2+b
    gradw1=-1*(y-a)*x1
    w1=w1-0.01*gradw1
    return w1
def update_w2(x1,x2,w1,w2,b,y):
    a=x1*w1+x2*w2+b
    gradw2=-1*(y-a)*x2
    w2=w2-0.01*gradw1
    return w2
def update_b(x1,x2,w1,w2,b):
    a = x1 * w1 + x2 * w2 + b
    gradb=(-1 * (y - a))
    b = b-0.01*gradb
    return b
for i in range(1000):#Epcoh
    for i in range(10):
        new_w1=update_w1(x1[i],x2[i],w1,w2,b)
        new_w2=update_w1(x1[i],x2[i],w1,w2,b)
        new_b=update_b(x1[i],x2[i],w1,w1,b)
        w1=new_w1
        w2=new_w2
        b=new_b
print(w1,w2,b)
while(True):
    a=float(input())
    c = float(input())
    a1 = a * w1 + c * w2 + b
    if(a>0.5):
        print(1)
    else:
        print(0)

