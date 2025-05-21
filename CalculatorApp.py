print("\n")
print("------------------Calculator App---------------")
print("\n")
print("Select Any one One Arithematic Operation to PErform: ")
print(" 1. Addition\n 2. Multiplication\n 3. Division\n 4. Substraction\n 5. Exit ")
print("\n")
choice= input(" ► Select any One Number (  1 / 2 / 3 / 4  / 5) : ")

if choice=="1":

    def add():
        print("\n------Addition Program-------")
        print("\n")
        x = int(input("Enter First Number: "))
        y = int(input("Enter Second Number: "))
        z=x+y
        return z
    print("The Addition of 2 Numbers is : ",add())

if choice=="2":

    def mul():
        print("\n------Multiplication Program-------")
        print("\n")
        a = int(input("ENTER FIRST NO. : "))
        b = int(input("ENTER SECOND NO. : "))
        c = a*b
        return c
    print("The Multiplication of Both Numbers are : ",mul())

if choice == "3":

    def div():
        print("\n------Division Program-------")
        print("\n")
        d = int(input("ENTER FIRST NO. : "))
        e = int(input("ENTER SECOND NO. : "))
        f = d/e
        return f
    print("The Division of Both Numbers are : ",div())

if choice == "4":
    def sub():
        print("\n------Substraction Program-------")
        print("\n")
        g = int(input("ENTER FIRST NO. : "))
        h = int(input("ENTER SECOND NO. : "))
        i = g-h
        return i
    print("The Substraction of Both Numbers are : ",sub())

if choice == "5":
    print("You hVe Terminated the session")
