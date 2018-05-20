tbd = {('mengyue', 18, 'girl'), ('zwm', 22, 'boy'), ('xiaoming', 1, 'boy'), ('xiaohong', 2, 'girl')}
if __name__ == "__main__":
    print(set(filter(lambda x: x[2] == 'boy', tbd)))
