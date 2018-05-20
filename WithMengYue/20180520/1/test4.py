from functools import reduce
tbd = {('mengyue', 18, 'girl'), ('zwm', 22, 'boy'), ('xiaoming', 1, 'boy'), ('xiaohong', 2, 'girl')}
if __name__ == "__main__":
    boy = (tuple(filter(lambda x: x[2] == 'boy', tbd)))
    print(boy)
    avr = reduce(lambda x, y: (x+y[1])/2, boy, boy[0][1])
    print(avr)
