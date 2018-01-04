def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1,num2):
    return num1 * num2


def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        return 0


def run_operation(operation, num1, num2):
    if (operation == 1):
        print("adding...")
        print(add(num1, num2))

    elif (operation == 2):
        print("subtracting...")
        print(sub(num1, num2))


    elif (operation == 3):
        print("multiplying...")
        print(add(num1, num2))

    elif (operation == 4):
        print("dividing...")
        print(div(num1, num2))


def main():

    user_input = False

    while not user_input:


        x = False
        while not x:
            try:
                num1 = int(input("What is Number 1?"))
                x = True

            except ValueError:
                print("Invalid Input. please try again...")

            except:
                print("something went wrong. please try again")


        y = False
        while not y:
            try:
                num2 = int(input("What is Number 2?"))
                y = True

            except ValueError:
                print("Invalid Input. please try again...")

            except:
                print("something went wrong. please try again")


        z = False
        while not z:

            try:
                operation= int(input("what do you want me to do? 1. add, 2. sub, 3. mul, 4. div? "))
                if operation <= 4:
                    z = True

                else:
                    print("invalid input. Please try again")

            except ValueError:
                print("Invalid Input. please try again...")

            except:
                print("something went wrong. please try again")


        run_operation(operation, num1, num2)

        #ask user to continue or exit

        a = input("""Do you want to do more calculations?
            Type 'y' or 'yes', if you want to do more.
            Otherwise type anything.""")

        if(a == "y" or a == "yes" or a == "Y" or a == "Yes" or a == "YES"):
            print("O.K. Do as many calculations as you like.")


        else:
            print("Thanks for using my calculator")
            user_input = True





main()
