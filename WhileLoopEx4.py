#Program for Generating  Mul Table for a Given Number
#WhileLoopEx4.py
n=int(input("Enter a number for generating mul table"))
if(n<=0):
    print("{} Invalid Num")
else:
    print("Mul table for:{}".format(n))
    i=1
    while(1<=10):
        print("\t\t{} x {}={}".format(n,i,n*i))
        i=i+1
    else:
        print("*"*50)
