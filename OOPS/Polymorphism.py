class A:
    classvar1 = 'Class Variable of Class A'

    def __init__(self):
        self.var1 = 'Inside Class A'
        self.classvar1 = 'Instance Variable of class A'
        print("It came here")

class B(A):
    classvar1 = 'Class Variable of Class B'

    def __init__(self):
        self.var1 = 'Inside Class B'
        self.classvar1 = 'Instance Variable of class B'
        print(B.classvar1)  # Access class variable of class B directly

b = B()
print(b.classvar1)
