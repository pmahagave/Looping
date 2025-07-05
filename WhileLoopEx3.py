#Program for Generating  all Even Numbers  within N   where N is +Ve
#WhileLoopEx3.py
n=int(input("Enter how many number u want to generate:"))
if(n<=0):
    print("\t{} Invalid Input".format(n))
else:
    print("Even number within{}".format(n))
    i=2
    while(i<=n):
        print("\t\t{}".format(i))
        i+=2
    else:
        print("*"*40)