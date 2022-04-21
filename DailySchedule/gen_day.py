yea = 2018
mon = 5
day = 21
lst_s = {1:31, 2:28, 3:31, 4:30,\
         5:31, 6:30, 7:31, 8:31,\
         9:30, 10:31, 11:30, 12:31}
with open('./day.txt', 'w') as f:
    for i in range(8):
        ll = ''
        for j in range(7):
            ll_one = str(yea) + '.' + str(mon) + '.' + str(day)
            if j == 6:
                ll = ll + ll_one
            else:
                ll = ll + ll_one + ' '
            if day == lst_s[mon]:
                if mon == 12:
                    yea = yea + 1
                    mon = 1
                    day = 1
                else:
                    mon = mon + 1
                    day = 1
            else:
                day = day + 1
        f.write(ll+'\n')
            
