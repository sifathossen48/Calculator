print("Welcome to Calculator project")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option=int(input("enter option for operation:"))
if option in range(1,5):
    n1=int(input("Enter 1st Number: "))
    n2=int(input("Enter 2nd Number: "))

    if option==1:
        print("addition: "+str(n1+n2))
    elif option==2:
        print("subtraction: "+str(n1-n2))
    elif option==3:
        print("multiplication: "+str(n1*n2))
    else :
        print("Division: "+str(float(n1/n2)))
else:
    print("invalid input")