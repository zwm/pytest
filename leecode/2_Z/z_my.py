def convert(s, numRows):
    def fn(s,numRows):
        if numRows == 1:
            return s
        len_ = 2*numRows-1
        s_new = s + " " * (len_-len(s))  ##不足长度用" "补齐
        s_temp = s[1:len_-1]
        return s_new[0]+s_new[-1]+fn(s_temp,numRows-1)
    if numRows==1:
        return s
    N = int(len(s)/(2*(numRows-1))) + 1
    # print("周期数：",N)
    # 每个周期有多少个字符
    len_ = 2*numRows-2
    # print("每个周期有字符个数:",len_)
    return_s = []
    for i in range(N):
        s_new = s[(i)*len_:(i+1)*len_]
        return_s_temp = fn(s_new,numRows)
        # print(return_s_temp)
        return_s.append(return_s_temp)
    print(return_s)
    ss = []
    for i in range(numRows):
        for j in range(N):
            ss += return_s[j][i*2:2*(i+1)]
    ss = "".join(ss).replace(" ","") 
    # print(ss)
    return ss

print (convert('abcdefghijklmn', 4))

