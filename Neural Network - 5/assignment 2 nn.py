w11_1,w11_2,w12_1,w12_2,w22_1,w22_2,w21_1,w21_2,b1_1,b1_2,b2_1,b2_2=0.1,-0.25,0.5,0.2,0.3,-0.4,0.6,-0.5,0.8,0.1,0.4,0.3
x1=[1,1,2,2,3,3,4,4,5,5]
x2=[2.2,2.4,2.5,2.7,2.8,3,3,3.3,3.4,3.7]
y1=[0,1,0,1,0,1,0,1,0,1,0]
y2=[1,0,1,0,1,0,1,0,1,0,1]
def update_w2(a,d,w):
    grad=a*d
    w=w-0.01*grad
    return w
for j in range(10000):
    for i in range(10):
        a1_1 = (x1[i] * w11_1) + (x2[i] * w12_1) + (1 * b1_1)
        a2_1 = (x1[i] * w21_1) + (x2[i] * w22_1) + (1 * b2_1)
        a1_2 = (a1_1 * w11_2) + (a2_1 * w12_2) + (1 * b1_2)
        a2_2 = (a1_1 * w21_2) + (a2_1 * w22_2) + (1 * b2_2)
        delta1_2=-1*(y1[i]-a1_2)
        delta2_2=-1*(y2[i]-a2_2)
        delta1_1=-1*((y1[i]-a1_2)*w11_2+(y2[i]-a2_2)*w21_2)
        delta2_1=-1*((y1[i]-a1_2)*w12_2+(y2[i]-a2_2)*w22_2)
        new_w11_2=update_w2(a1_1,delta1_2,w11_2)
        new_w12_2=update_w2(a2_1,delta1_2,w12_2)
        new_w21_2=update_w2(a1_1,delta2_2,w21_2)
        new_w22_2=update_w2(a2_1,delta2_2,w22_2)
        new_w11_1=update_w2(x1[i],delta1_1,w11_1)
        new_w12_1=update_w2(x2[i],delta1_1,w12_1)
        new_w21_1=update_w2(x1[i],delta2_1,w21_1)
        new_w22_1=update_w2(x2[i],delta2_1,w22_1)
        new_b1_1=update_w2(1,delta1_1,b1_1)
        new_b2_1=update_w2(1,delta2_1,b2_1)
        new_b1_2=update_w2(1,delta1_2,b1_2)
        new_b2_2=update_w2(1,delta2_2,b2_2)
        b1_1, b1_2, b2_1, b2_2=new_b1_1,new_b1_2,new_b2_1,new_b2_2
        w11_1,w12_1,w21_1,w22_1=new_w11_1,new_w12_1,new_w21_1,new_w22_1
        w11_2,w12_2,w21_2,w22_2=new_w11_2,new_w12_2,new_w21_2,new_w22_2
print(w11_1,w12_1,w21_1,w22_1,w11_2,w12_2,w21_2,w22_2,b1_1,b1_2,b2_1,b2_2)
for i in range(10):             #checking the Neural Network
    '''a1_1 = (x1[i] * w11_1) + (x2[i] * w12_1) + (1 * b1_1)
    a2_1 = (x1[i] * w21_1) + (x2[i] * w22_1) + (1 * b2_1)
    y1 = (a1_1*w11_2)+(a2_1*w12_2)+(1*b1_2)
    y2 = (a2_1*w22_2)+(a1_1*w21_2)+(1*b2_2)
    print(1 if y1 > 0.5 else 0, 1 if y2 > 0.5 else 0)'''
    z=int(input())
    y=float(input())
    a1_1 = (x1[i] * w11_1) + (x2[i] * w12_1) + (1 * b1_1)
    a2_1 = (x1[i] * w21_1) + (x2[i] * w22_1) + (1 * b2_1)
    y1 = (a1_1 * w11_2) + (a2_1 * w12_2) + (1 * b1_2)
    y2 = (a2_1 * w22_2) + (a1_1 * w21_2) + (1 * b2_2)
    print(1 if y1 > 0.5 else 0, 1 if y2 > 0.5 else 0)
