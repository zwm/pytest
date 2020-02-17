
class X(object):
        def __init__(self):
                print ("enter X")
                print ("    This is Class X!")
                print("leave X")

class A(X):
        def __init__(self):
                print ("enter A")
                super(A, self).__init__()  # new
                print("leave A")


class B(X):
        def __init__(self):
                print("enter B")
                #super(B, self).__init__()  # new
                print("leave B")


class C(A,B):
        def __init__(self):
                print("enter C")
                super(C, self).__init__()
                print("leave C")

print(C.mro())
print("------------")
c = C()

# B加super时，可以执行到X
# B不加super时，只执行到B
# 也就是super并不一定保证执行到真正的父类，也可能只执行到平级类，这应该是不常用的用法吧

