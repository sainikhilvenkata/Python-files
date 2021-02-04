x=int(input())
y=int(input())
a=1
while(a<=y):
    for i in range(a):
        print(x,end='')
    x=x+1
    print()
    a=a+1
y=y-1
a=1
x=x-1
while(a<=y):
    x=x-1
    for i in range(y):
        print(x,end='')
    y=y-1
    print()
    
