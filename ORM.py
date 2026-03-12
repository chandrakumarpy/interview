class A:
    def fun1(self):
        print("A")

class B(A):
    def fun1(self):
        print("B")

class C(A):
    def fun1(self):
        print("C")

class D(C, B):
    def fun1(self):
        super(C, self).fun1()

obj = D()
obj.fun1() # hear ansower is b, if 15 th line remove c,self we get C 
#-----------------------------------------------------------
'''class D(C, B):
    pass''' # You will get ans C