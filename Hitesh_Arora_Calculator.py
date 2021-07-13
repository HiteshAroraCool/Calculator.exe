## the program where everything happens
def calc(a, b, ch):
        if ch == 1:
            print("The Sum is: ", a + b)
            print("\n")
            cal()
        elif ch == 2:
            print("\nThe Difference is: ", a - b)
            print("\n")
            cal()
        elif ch == 3:
            print("\nThe Product is: ", a * b)
            print("\n")
            cal()
        elif ch == 4:
            if b != "0":
                try:
                    print("\nThe Quotient is: ", a / b)
                    print("\n")
                    cal()
                except:
                    print("Can't divide by 0")
                    cal()

            else:
                cal()
        elif ch == 5:
                print("\nThe Exponent is: ", a ** b)
                print("\n")
                cal()
        elif ch == 6:
            print("\nThe Floor value is: ", a // b)
            print("\n")
            cal()
        elif ch == 7:
            print("\nThe Remainder is: ", a % b)
            print("\n")
            cal()
        else:
            cala()
    
    


##asking for the choice
def cala():
    print("\nCalculator")
    try:        
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
    except ValueError:
        print("Error!!! Please enter a vaild value.\n")
        cal()

    print("\nMath oprations:")
    print("1.Addition\n2.Subraction\n3.Multiplication\n4.Division\n5.Exponent\n6.Floor Division\n7.Modulus")
    try:
            ch = int(input("\nEnter your choice:"))
    except ValueError:
            print("Please provide a vaild choice.")
            cala()
            
    if ch > 7 or ch==0:
        try:
            print("Enter between 1 to 7")
            cala()
        except ValueError:
            print("Please provide a vaild integer.")
            cala()
    else:
        calc(a, b, ch)


##asking the cal to run agian
def cal():
    y = str(input("Do you want run it again?(yes or no)\n"))
    
    if y == "yes"or y=="y" or y=="Y" or y=="YES" or y=="Yes":
        cala()
    elif y == "no" or y=="n" or y=="N" or y=="NO" or y=="No":
        input("pass ENTER to exit.")
        exit()
    else:
        print("Wrong choice")
        cal()

        
##main program
ac = str(input("Do you want to run the calculator?\n"))
if ac == "yes" or ac=="y" or ac=="Y" or ac=="YES" or ac=="Yes":
    cala()
elif ac == "no" or ac=="n" or ac=="N" or ac=="NO" or ac=="No":
    input("pass ENTER to exit.")
    exit()
else:
    try:
        print("Wrong choice")
        cal()
    except:
        print("Error")
        cal()
