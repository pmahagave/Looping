

def readvalues(op):
    print("Enter Two Values for '{}'".format(op))
    x,y=float(input()),float(input())
    return x,y
def menu():
    print("\t\tArithmatic Operation")
    print("\t\t1.Addition")
    print("\t\t2.Substraction")
    print("\t\t3.Multiplication")
    print("\t\t4.Division")
    print("\t\t5.floordivision")
    print("\t\t6.Modulo Division")
    print("\t\t7.Exponentiation")
    print("\t\t8.Exit")

#Anonymous function defination
addop=lambda k,v:k+v
subop=lambda k,v:k-v
mulop=lambda k,v:k*v
divop=lambda k,v:k/v
FloorDivop=lambda k,v:k//v
modop=lambda k,v:k%v
powop=lambda k,v:k**v

#Main Program

While(True):
    menu()
    ch=input("Enter Ur choice")
    if(ch.isdigit())
        match(int(ch)):
            case1:
                 a,b=readvalues("Addition")
                 res=addop(a,b)