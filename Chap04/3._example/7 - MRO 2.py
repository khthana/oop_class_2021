class A:
    def rk(self):
        print("In class A")

class B:
    def rk(self):
        print("In class B")

class C:
    def rk(self):
        print("In class C")

class D(B, C):
    pass

r = D()
r.rk()

