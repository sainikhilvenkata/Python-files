class Bank:
    _accno=12345
    branch ="Thanjavur"
    name ="Nikhil"
    def __init__(self):
        
        self.amount=0
    def deposit(self,a):
        self.amount+=a
        print(self.amount)
    def withdraw(self,a):
        self.amount-=a
        print(self.amount)
    def getitem(self):
        p=input("enter name")
        self.name=p
        q=input("enter branch")
        self.branch=q
    def putitem(self):
        print(self.name,self.branch)
        
a=Bank()
setattr(a,'allowance',100) 
print(getattr(a,'allowance'))

a.deposit(1000)
a.withdraw(100)
a.getitem()
a.putitem()


        
