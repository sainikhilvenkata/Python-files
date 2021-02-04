n=int(input())
u =list(input().split())
x=u[0]
y=u[1]
v=ord(y)-ord(x)+1
d=list(input().split())
p=int(d[0])
q=int(d[1])

z=q-p+1
if z<=10 and v<=26 and n>=1 and n<100 and z>=0 and v>=2:
    res1=n*(v*v)
    res2=(z)**4-(z)-(4*z)
    res=res1*res2
    print(res)
