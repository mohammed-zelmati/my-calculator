# The main menu of choices
def main_menu():
    print("\n========== Welcome to the calculator! ===========\n")
    print("========== 1. Perform an operation   ============") 
    print("========== 2. View history ======================") 
    print("========== 3. Clear history =====================") 
    print("========== 4. Exit ==============================")

# Asks the user to enter three numbers and handle errors 
def get_numbers():
    while True:
        try:
            num1 = float(input("========= Enter the first number: "))
            num2 = float(input("========= Enter the second number: "))
            num3 = float(input("========= Enter the third number: "))
            return num1, num2, num3
        except ValueError:
            print("\n======= Invalid input. Please enter valid numbers. ========\n")

# Asks the user to enter an operator and handle errors
def get_operations():
    while True:
        operation1 = input("\n===== Enter the desired operation (+, -, *, /): ")
        operation2 = input("\n===== Enter the desired operation (+, -, *, /): ")
        if operation1 in ['+', '-', '*', '/'] and operation2 in ['+', '-', '*', '/']:
            return operation1, operation2
        else:
            print("\n========= Invalid operation. Please enter two of the following operations: +, -, *, / : ")

# Do the calculations of three numbers with two digits after the decimal point and handle divide-by-zero errors
def calculate(num1, num2, num3, operation1, operation2):
    #  Probabilities:(+ +) (+ -)(+ *)(+ /)..... (- +) (- *) (- -)(- /).....(* +) (* *) (* -)(* /) ....(/ +) (/ *) (/ -)(/ /)
    if operation1 == '+':
        if operation2 == '+':
            return round(num1 + num2 + num3, 2)
        elif operation2 == '-':
            return round(num1 + num2 - num3, 2)
        elif operation2 == '*':
            return round((num1 + num2) * num3, 2)
        elif operation2 == '/':
            if num3 != 0:
                return round((num1 + num2 )/ num3, 2)
            else:
                print("\n=========== Error: Division by zero. ===========\n")
                return None
    elif operation1 == '-':
        if operation2 == '+':
            return round(num1 - num2 + num3, 2)
        elif operation2 == '-':
            return round(num1 - num2 - num3, 2)
        elif operation2 == '*':
            return round((num1 - num2) * num3, 2)
        elif operation2 == '/':
            if num3 != 0:
                return round((num1 - num2 )/ num3, 2)
            else:
                print("\n=========== Error: Division by zero. ===========\n")
                return None
    elif operation1 == '*':
        if operation2 == '+':
            return round((num1 * num2) + num3, 2)
        elif operation2 == '-':
            return round((num1 * num2) - num3, 2)
        elif operation2 == '*':
            return round((num1 * num2) * num3, 2)
        elif operation2 == '/':
            if num3 != 0:
                return round((num1 * num2 )/ num3, 2)
            else:
                print("\n=========== Error: Division by zero. ===========\n")
                return None
    elif operation1 == '/':
        if operation2 == '+':
            if num2 != 0 and num3 != 0:
                return round((num1 / num2) + num3, 2)
            else:
                print("\n=========== Error: Division by zero. ===========\n") 
                return None
        elif operation2 == '-':
            if num2 != 0 :
                return round((num1 / num2) - num3, 2)
            else: print("\n=========== Error: Division by zero. ===========\n")
            return None
        elif operation2 == '*':
            if num2 != 0 :
                return round((num1 / num2) * num3, 2)
            else: print("\n=========== Error: Division by zero. ===========\n")
            return None
        elif operation2 == '/':
            if num2 != 0 and num3 != 0:
                return round(num1 / num2 / num3, 2)
            else:
                print("\n=========== Error: Division by zero. ===========\n")
                return None

# View history if it exists or not
def show_history(history):
    if history:
        print("\n=========== Operations recorded. ===========\n")
        for i in history:
            print(i)
    else:
        print("\n=========== No operations recorded. ===========\n")
# Clear the history
def clear_history():
    return []

def main():
    history = []
    while True:
        main_menu()
        choice = input("\n========== Enter your choice (number between 1 and 4) : ")
        #  Choice 1 : Perform an operation
        if choice == '1':
            num1, num2, num3 = get_numbers()
            operation1, operation2 = get_operations()
            result = calculate(num1, num2, num3, operation1, operation2)
            if result is not None:
                print(f"\n========= The result of:\n {num1} {operation1} {num2} {operation2} {num3} = {result} ")
                history.append(f"{num1} {operation1} {num2} {operation2} {num3} = {result}")
        # choice 2 : View history
        elif choice == '2':
            show_history(history)
        # choice 3 : delete history  
        elif choice == '3':
            history = clear_history()
            print("\n========== The history has been cleared==========\n")
        # choice 4 : exit the script
        elif choice == '4':
            print("\n=========== Goodbye!===========================\n")
            break
        else:
            print("\n=========== Invalid choice.")

# Démarrer le script
if __name__ == "__main__":
    main()