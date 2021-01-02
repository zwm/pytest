

def op_multi(idx, a, b):
    if idx == 0:
        return (a + b)
    elif idx == 1:
        return (a - b)
    elif idx == 2:
        return (a * b)
    else:
        if b == 0: # tbd!!!
            return 99999999
        return (a / b)

# check 24, + - * /
def check24(a, b, c, d):
    for op1 in range(4):
        for op2 in range(4):
            for op3 in range(4):
                for bra in range(6):
                    if bra == 0: # (a b) c d
                        r1 = op_multi(op1, a, b)
                        r2 = op_multi(op2, r1, c)
                        r3 = op_multi(op3, r2, d)
                    elif bra == 1: # a (b c) d
                        r1 = op_multi(op2, b, c)
                        r2 = op_multi(op1, a, r1)
                        r3 = op_multi(op3, r2, d)
                    elif bra == 2: # a b (c d)
                        r1 = op_multi(op3, c, d)
                        r2 = op_multi(op1, a, b)
                        r3 = op_multi(op2, r1, r2)
                    elif bra == 3: # (a b) (c d)
                        r1 = op_multi(op1, a, b)
                        r2 = op_multi(op3, c, d)
                        r3 = op_multi(op2, r1, r2)
                    elif bra == 4: # a ((b c) d)
                        r1 = op_multi(op2, b, c)
                        r2 = op_multi(op3, r1, d)
                        r3 = op_multi(op1, a, r2)
                    else: # a (b (c d))
                        r1 = op_multi(op3, c, d)
                        r2 = op_multi(op2, b, r1)
                        r3 = op_multi(op1, a, r2)
                    # check 24
                    if abs(r3 - 24) < 0.0001:
                        print("%d |%d| %d |%d| %d |%d| %d    (%d)\n"%(a, op1, b, op2, c, op3, d, bra))
                        return 1
    return 0

# a b c d select
def main_loop(ui):
    ui_len3 = [0,0,0]
    ui_len2 = [0,0]
    for c41_idx in range(4): # c41, select a
        idx = c41_idx
        a = ui[idx]
        for i in range(3):
            idx = (c41_idx + i + 1)%4
            ui_len3[i] = ui[idx]
        for c31_idx in range(3): # c31, select b
            idx = c31_idx
            b = ui_len3[idx]
            for i in range(2):
                idx = (c31_idx + i + 1)%3
                ui_len2[i] = ui_len3[idx]
            for c21_idx in range(2): # c21, select c and d
                idx = (c21_idx + 0)%2
                c = ui_len2[idx]
                idx = (c21_idx + 1)%2
                d = ui_len2[idx]
                # proc
                is24 = check24(a, b, c, d)
                if is24 == 1:
                    return 1
    # else
    return 0
    
# user input
#user_input = [1, 3, 4, 6]
#user_input = [3, 3, 8, 8]
user_input = [4, 1, 8, 7]

final_out = main_loop(user_input)
if (final_out == 1):
    print("Check 24 True!\n")
else:
    print("Check 24 FAILED!\n")


