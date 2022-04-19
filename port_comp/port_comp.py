

fdir = './'
fnew = fdir + 'new.txt'
fold = fdir + 'hw2.txt'

pnew = []
pold = []
new_add = []
new_keep = []
old_del = []

# new
with open(fnew, 'r') as f:
    for ln in f:
        ln = ln.strip()
        pnew.append(ln)
# old
with open(fold, 'r') as f:
    for ln in f:
        ln = ln.strip()
        pold.append(ln)
for p in pnew:
    if p in pold:
        new_keep.append(p)
    else:
        new_add.append(p)

for p in pold:
    if p in pnew:
        pass
    else:
        old_del.append(p)


print('--- new_keep  ---------------')
for p in new_keep:
    print(p)
print('--- new_add   ---------------')
for p in new_add:
    print(p)
print('--- old_del   ---------------')
for p in old_del:
    print(p)


