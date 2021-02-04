class A:
 a=0
 def count(p):
     global a
     yield p.a
     p.a =p.a+1
     print('a value is',p.a)



class B:
    b=0
    def count(q):
        global b
        yield b
        b=q.b+1
        print(b)
x=A()
y=B()
print("yes")
x.count()
y.count()
    
    
