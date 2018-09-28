import random

# data module
# 10~100, gap 10, 10
# 100~1000, gap 100, 10
# 1000~4096, gap 1000, 4

data_path = 'E:\Code\data_src'
path_delimiter = '\\'
case_idx = 0

# 0~19: 1~5 byte, all 0, all 1, 55, aa, 4*5=20
cont_val = ['00', 'FF', '55', 'AA']
for i in range(5):
    for j in range(len(cont_val)):
        tmp = cont_val[j]
        fname = data_path + path_delimiter + ('%0d'%case_idx)
        case_idx = case_idx + 1
        with open(fname, 'w') as f:
            f.write(tmp)
            f.write('\n')
            for k in range(i):
                f.write(tmp)
                f.write('\n')

# 20~29: 10~100, gap 10, 10
for i in range(10):
    fname = data_path + path_delimiter + ('%0d'%case_idx)
    case_idx = case_idx + 1
    with open(fname, 'w') as f:
        for k in range((i+1)*10):
            tmp = random.randint(0,255)
            tmp = hex(tmp)
            if len(tmp)==3:
                tmp = '0'+tmp[2]
            else:
                tmp = tmp[2:4]
            f.write((tmp))
            f.write('\n')

# 30: sequence 100
fname = data_path + path_delimiter + ('%0d'%case_idx)
with open(fname, 'w') as f:
    for i in range(100):
        f.write('%02x\n'%i)
case_idx = case_idx + 1
