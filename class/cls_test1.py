# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 20160415

__metaclass__ = type # super函数只在新式类中起作用

class Bird(object):
    def __init__(self):
        self.hungry = True
    def eat(self):
        if self.hungry:
            print 'Aaaah...'
            self.hungry = False
        else:
            print 'No, thanks!'
'''
# 直接重写构造方法，会覆盖父类构造方法，可能会造成父类某些方法不能正常运行。
class SongBird(Bird):
    def __init__(self):
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
'''

'''
# 调用未绑定的超类构造方法
# 这个方法是历史遗留问题，目前版本，使用super函数
# 因为调用实例的方法时，该方法的self参数会被自动绑定到实例上，这称为绑定方法
class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
'''

#'''
# 使用super函数
# 它使用在新式类中，我们应该使用新式类。
# 当前的类和对象可以作为super函数的参数使用，调用函数返回的对象的任何方法都是调用超类的方法，而不是当前类的方法。
class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__()
        self.sound = 'Squawk!'
    def sing(self):
        print self.sound
#'''



if __name__ == '__main__':
    bird = Bird()
    songbird = SongBird()
    bird.eat()
    bird.eat()
    songbird.sing()
    songbird.eat()
    songbird.eat()

