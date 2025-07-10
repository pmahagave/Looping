#AnonymousFunEx2.py
palindrome=lambda value:"Palindrome" if value==value[::-1]else \
    "Not Palindrome"

#Main Program
value=input("Enter Any Value:")
res=palindrome(value)
print("{} is {}".format(value,res))