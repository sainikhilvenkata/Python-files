a=int(input())
l=0
X=[]
Y=[]
X1=[]
Y1=[]
X2=[]
Y2=[]
t2=0
t3=0
for i in range(1,a+1):
    b=input()
    c=input()
    X.append(b)
    Y.append(c)
print("Enter Points for cluster")
k1=int(input())
k2=int(input())
def f1(k1,k2):
    for i in range(1,a+1):
        b=int(int(X[i])-int(X[k1]))**2
        c=(int(Y[i])-int(Y[k1]))**2
        t1=float((b+c)**0.5)
        b=(int(X[i])-int(X[k2]))**2
        c=(int(Y[i])-int(Y[k2]))**2
        t=float((b+c)**0.5)
        if(min(t1,t)==t1):
            X1.append(i)
        else:
            Y1.append(i)
        for i in X1:
            t2=t2+int(X[i])
            t3=t3+int(Y[i])
        t2=float(t2/len(X1))
        t3=float(t3/len(Y1))
        X.append(t2)
        Y.append(t3)
        k1=len(X)+1
        for i in Y1:
            t2=t2+X[i]
            t3=t3+Y[i]
        t2=t2/len(X1)
        t3=t3/len(Y1)
        X.append(t2)
        Y.append(t3)
        k2=len(X)+1
for i in range(0,4):
    f1(k1,k2)
print("Cluster 1 is",X1)
print("Cluster 2 is",Y1)


