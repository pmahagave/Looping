#Program for Generating  N to 1 Numbers where N is +Ve
#WhileLoopEx2.py

'''n=int(input("Enter how many number u want to generate:"))
if(n<0):
    print("\t{} is Invalid Input".format(n))
else:
    print("Number from {} to 1".format(n))
    i=n
    while(n>=1):
        print("\t\t{}".format(n))
        n-=1'''

num=int(input("Enter a number:"))
rev=0

while num != 0:
    digit = num % 10
    rev= rev * 10 + digit
    num = num // 10
print("Reversed num:",rev)


