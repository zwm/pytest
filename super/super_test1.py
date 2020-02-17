class A():
    def __init__(self):
        print('enter A')
        print('leave A')
class X():
        def __init__(self):
                print('enter X')
                print('leave X')
        pass
class F():
    def __init__(self):
        print('enter F')
        super().__init__()
        print('leave F')

class B( F, A):
#class B(A):
    def __init__(self):
        print('enter B')
        super(B,self).__init__()
        # F.__init__(self)
        print('leave B')


class C(A):
    def __init__(self):
        print('enter C')
        super().__init__()
        print('leave C')


class D(B, C):
    def __init__(self):
        print('enter D')
        super().__init__()
        print('leave D')


#d = D()
b= B()
print(B.mro())
