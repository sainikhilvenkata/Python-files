x=5
j=1
for i in range(4,-1,-1):
    p=i
    while(p>0):
        print("*",end='')
        p=p-1
    y=0
    while(j>y):
        print(".",end='')
        y=y+1
    j=j+2
    p=i
    while(p>0):
        print("*",end='')
        p=p-1
    print()
x=5
j=1
l=x-1
for i in range(0,4):
    p=i+1
    
    while(p>0):
        print("*",end='')
        p=p-1
    k=(2*l)-1
    while(k>0):
        print(".",end='')
        k=k-1
    l=l-1
    p=i+1
    
    while(p>0):
        print("*",end='')
        p=p-1
    print()
    
