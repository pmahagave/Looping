#Program for Generating 1 to N Numbers where N is +Ve
#WhileLoopEx1.py
n=int(input("Enter how many number u want to generate:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("\t{} is valid Input".format(n))
    i=1
    while(i<=n):
        print("\t{}".format(i))
        i=i+1
    else:
        '''print("I am else part of while loop")'''
    print("I am after while loop")


