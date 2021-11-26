def check(num):
    for n in range(2,num,1):
        tempnum=num/n
        if tempnum.is_integer():
            return False
    return True

x=1
list=[]
prev=int(-10)
str=""
while True:
    x=x+1
    if check(x):
        list.append(x)
        if x-2==prev:
            str="Kaksik!"
        print("{}.\t{}\t{}".format(len(list),x,str))
        str=""
        prev=x
    