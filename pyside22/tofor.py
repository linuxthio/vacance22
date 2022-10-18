

d=[1,2,4]
f=[90,2,3,11,'fe','sed','dwq']

def boucle(s,x):
    ma=max(s,x)
    for i in range(len(ma)):
        if i<len(s):
            print('1er :',s[i])
        if i<len(x):
            print('2e :',x[i])

boucle(d,f)
