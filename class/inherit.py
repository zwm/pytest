# -*- coding: utf-8 -*-
# Author : zwm
# Time   : 20160416

__metaclass__ = type # super函数只在新式类中起作用

class SchoolMember(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print 'init SchoolMember: ', self.name
    def tell(self):
        print 'name: %s; age: %s' % (self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print 'init Teacher: ', self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'salary: %s' % (self.salary)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print 'init Student: ', self.name
    def tell(self):
        SchoolMember.tell(self)
        print 'marks: %s' % (self.marks)

if __name__ == '__main__':
    t = Teacher('Yang', 20, 1000)
    s = Student('Ming', 12, 86)
    members = [t, s]
    print
    for member in members:
        member.tell()
