class User:
    def __init__(self, first_name, last_name,  sex='man', age=18):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age

    def describe_user(self):
        print('USER DESCRIPTION')
        print('Name: %s.%s'%(self.first_name, self.last_name))
        print('Sex : %s'%self.sex)
        print('Age : %d'%self.age)

    def greet_user(self):
        print('Hello, my dear %s.%s!' % (self.first_name, self.last_name))

print("-------------------TEST USER 1------------------")
usr1 = User('Cillayue', 'Meng', 'girl', 18)
usr1.describe_user()
usr1.greet_user()
print("-------------------TEST USER 2------------------")
usr2 = User('William', 'Zhang', 'boy', 22)
usr2.describe_user()
usr2.greet_user()
