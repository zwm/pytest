import datetime

def isPureNum (dat_str):
    # if any dismatch, return 1
    for i in range(len(dat_str)):
        if dat_str[i] != '0' and dat_str[i] != '1' and\
           dat_str[i] != '2' and dat_str[i] != '3' and\
           dat_str[i] != '4' and dat_str[i] != '5' and\
           dat_str[i] != '6' and dat_str[i] != '7' and\
           dat_str[i] != '8' and dat_str[i] != '9':
               return 1
    # if all match, return 0
    return 0

def isNarcissusNum (dat_str):
    dat_len = len(dat_str)
    if dat_len > 9:
        return 2    # 2: exceed range
    sss = 0
    for i in range (dat_len):
        tmp = int(dat_str[i])
#        print ("tmp idx %d: %d"%(i, tmp)) 
        sss = sss + tmp**dat_len
#        print ("sss idx %d: %d" % (i, sss))
    if sss == int(dat_str):
        return 0    # 0: is Narcissus Number
    else:
        return 1    # 1: not Narcissus Number

    
if __name__ == "__main__":
    print("Program Init ...")
    print("    note : input [EXIT] to quit!")
    while (1):
        # start
        while(1):
            num_start = input("Please input START number :")
            if num_start == "":
                break
            if num_start == "EXIT":
                break
            if isPureNum (num_start) == 0:  # right
                break
            else:
                print ("Your input %s is not a number, please input again!"%num_start)
        # end
        while(1):
            num_end   = input("Please input END   number :")
            if num_end == "":
                break
            if num_end == "EXIT":
                break
            if isPureNum (num_end) == 0:  # right
                break
            else:
                print ("Your input %s is not a number, please input again!"%num_end)
        if (num_start == "") or (num_end == "") or (int(num_end) >= int(num_start)):
            break
        else:
            print ("num_start:%s is less than num_end:%s ! Please input again"%(num_start, num_end))

    # process
    if num_start == "" and num_end == "":
        num_start = "100"
        num_end = "999"
    elif num_start == "" and num_end != "":
        num_start = num_end
    elif num_start != "" and num_end == "":
        num_end = num_start
    print ("[START]: from %s to %s, narcissus num:" % (num_start, num_end))
    print ("[PROCESS]: analysis ongoing ...")
    rrr = int(num_end) - int(num_start) + 1
    dat_st = int(num_start)
    prog_start_time = datetime.datetime.now()
    for i in range (rrr):
        tmp = str(dat_st+i)
        if isNarcissusNum(tmp) == 0:
            print(tmp)
    prog_end_time = datetime.datetime.now()
    print ("[END]: analysis end!")
    print ("[TIME]: %d seconds!"%(prog_end_time - prog_start_time).seconds)
