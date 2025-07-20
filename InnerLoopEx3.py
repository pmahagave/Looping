#InnerLoopEx3.py
i=1
while(i<=5):
    print("outer Loop:Value of i=",i)
    for j in range(3,0,-1):
        print("Inner Loop:Value of j=",j)
    else:
        print("\tCame out off Inner Loop")
        i=i+1
else:
    print("came out off outer loop")
