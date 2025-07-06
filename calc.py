def words():
    print("A SIMPLE CALCULATOR")
   
def calculator():

    print("\n-Select an operation-")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input ("Enter your choice [1 , 2 , 3 , 4]: ")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        try:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        except ZeroDivisionError:
            print("Error: You cannot divide by zero bro!")
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    words()
    calculator()
