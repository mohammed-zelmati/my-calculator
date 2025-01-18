# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#                                                                                                           |||||
# Project to make a calculator allowing the user to write mathematical expressions and evaluate them.       |||||
# This program must ask the user for several pieces of information, three integers or decimals, as well     |||||
# as the type of operation desired (+ , / , * ,  - , **).                                                   |||||
# This calculator can perform the requested operations and handle any errors like incorrect entries or      |||||
# illegal operations and provide explicit error messages.                                                   |||||
# Respecting the order of operational priorities.                                                           |||||
#                                                                                                           |||||
# |||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


# The main menu of choice
def main_menu():
    print("\n====&&&&&&====== Welcome to the calculator! ======&&&&&&=====\n")
    print("========== 1. Perform an operation ==============") 
    print("========== 2. View history ======================") 
    print("========== 3. Clear history by line =============") 
    print("========== 4. Clear all history =================")
    print("========== 5. Exit ==============================")

# Asks the user to enter three numbers and handle errors 
def get_numbers():
    while True:
        try:
            num1 = float(input("||||||||||| Enter the first number: "))
            num2 = float(input("||||||||||| Enter the second number: "))
            num3 = float(input("||||||||||| Enter the third number: "))
            return num1, num2, num3
        except ValueError:
            print("\n======= Invalid input. Please enter valid numbers. ========\n")

# Asks the user to enter an operator and handle errors
def get_operations():
    while True:
        operation1 = input("\n||||||||||| Enter the desired operation (+, -, *, /, **): ")
        operation2 = input("\n||||||||||| Enter the desired operation (+, -, *, /, **): ")
        if operation1 in ['+', '-', '*', '/', '**'] and operation2 in ['+', '-', '*', '/', '**']:
            return operation1, operation2
        else:
            print("\n||||||||||| Invalid operation. Please enter one of the following operations: +, -, *, /, ** : ")

# Calculation of three numbers and two operations [+ , * , - , / , **]
def calculate(num1, num2, num3, operation1, operation2): 
    if operation1 == "**" and operation2 == "**" :
        result1 = num1 ** num2 
        result2 = result1 ** num3
    elif operation1 == "**" and operation2 == "*":
        result1 = num1 ** num2
        result2 = result1 * num3
    elif operation1 == "**" and operation2 == "/":
        result1 = num1 ** num2
        if num3 != 0 :   
            result2 = result1 / num3
        else: 
            print("Error : Invalid devision zero !")    
    elif operation1 == "**" and operation2 == "+":
            result1 = num1 ** num2
            result2 = result1 + num3
    elif operation1 == "**" and operation2 == "-":
            result1 = num1 ** num2
            result2 = result1 - num3  

    elif operation1 == "*" and operation2 == "**" :
        result1 = num2 ** num3
        result2 = num1 * result1
    elif operation1 == "*" and operation2 == "*":
        result2 = num1 * num2 * num3
    elif operation1 == "*" and operation2 == "/":
        result1 = num1 * num2
        if num3 != 0 :   
            result2 = result1 / num3
        else: 
            print("Error : Invalid devision zero !")    
    elif operation1 == "*" and operation2 == "+":
            result1 = num1 * num2
            result2 = result1 + num3
    elif operation1 == "*" and operation2 == "-":
            result1 = num1 * num2
            result2 = result1 - num3  

    elif operation1 == "/" and operation2 == "**" :
        result1 = num2 ** num3
        if result1 != 0:
            result2 = num1 / result1
        else: print("Error : Invalid devision zero !")    
    elif operation1 == "/" and operation2 == "*":
        result1 = num2 * num3
        if result1 != 0:
            result2 = num1 / result1
        else: print("Error : Invalid devision zero !") 
    elif operation1 == "/" and operation2 == "/":
        if num3 != 0 and num2 != 0:
            result1 = num1 / num2
            result2 = result1 / num3
        else: 
            print("Error : Invalid devision zero !")    
    elif operation1 == "/" and operation2 == "+":
        if num2 != 0:
            result1 = num1 / num2
            result2 = result1 + num3
        else: print("Error : Invalid devision zero !")    
    elif operation1 == "/" and operation2 == "-":
        if num2 != 0:
            result1 = num1 / num2
            result2 = result1 - num3  

    elif operation1 == "+" and operation2 == "**" :
        result1 = num2 ** num3
        result2 = num1 + result1   
    elif operation1 == "+" and operation2 == "*":
        result1 = num2 * num3
        result2 = num1 + result1
    elif operation1 == "+" and operation2 == "/":
        if num3 != 0 :
            result1 = num2 / num3
            result2 = num1 + result1
        else: 
            print("Error : Invalid devision zero !")    
    elif operation1 == "+" and operation2 == "+":
        result2 = num1 + num2 + num3    
    elif operation1 == "+" and operation2 == "-":
        result2 = num1 + num2 - num3    

    elif operation1 == "-" and operation2 == "**" :
        result1 = num2 ** num3
        result2 = num1 - result1   
    elif operation1 == "-" and operation2 == "*":
        result1 = num2 * num3
        result2 = num1 - result1
    elif operation1 == "-" and operation2 == "/":
        if num3 != 0 :
            result1 = num2 / num3
            result2 = num1 - result1
        else: 
            print("Error : Invalid devision zero !")    
    elif operation1 == "-" and operation2 == "+":
        result2 = num1 - num2 + num3    
    elif operation1 == "-" and operation2 == "-":
        result2 = num1 - num2 - num3       

    return round(result2, 2)

# View history if it exists or not
def show_history(history):
    if history:
        print("\n||||||||||| Operations recorded. |||||||||||\n")
        for i in history:
            print(i)
    else:
        print("\n||||||||||| No operations recorded. |||||||||||\n")

# Clear all history
def clear_history():
    return []

# Delete the history by line
def clear_history_line(history):

        clear_lines = input("Enter the numbers of the lines to be deleted (separated by commas): ")
        try:
            line_numbers = [int(num.strip()) for num in clear_lines.split(',')]
            line_numbers.sort(reverse=True) # Sort line numbers in descending order to avoid index errors
            for line_num in line_numbers:
                if 1 <= line_num <= len(history):
                    del history[line_num - 1]
                else:
                    print(f"||||||||||| Invalid line number: {line_num}")
            print("||||||||||| History after deletion : ", history)
        except ValueError:
            print("||||||||||| Invalid input, please enter valid line numbers separated by commas.")

# Run the script 
def main():
    history = []
    while True:
        main_menu()
        choice = input("\n ||||||||||| Enter your choice (number between 1 and 5) : ")
        #  Choice 1 : Perform an operation
        if choice == '1':
            num1, num2, num3 = get_numbers()
            operation1, operation2 = get_operations()
            result = calculate(num1, num2, num3, operation1, operation2)
            if result is not None:
                print(f"\n||||||||||| The result of:\n {num1} {operation1} {num2} {operation2} {num3} = {result} ")
                history.append(f"{num1} {operation1} {num2} {operation2} {num3} = {result}")
        # choice 2 : View history
        elif choice == '2':
            show_history(history)
        # choice 3 : delete history by line 
        elif choice == '3':
            clear_history_line(history)
            print("\n||||||||||| Removed the selected rows from the history \n")
        # choice 3 : delete all history
        elif choice == '4':
            history = clear_history()
            print("\n||||||||||| All history is cleared =\n")
        # choice 5 : exit the script
        elif choice == '5':
            print("\n|||||&&&&&&&&&&&&&&&&&& Goodbye! &&&&&&&&&&&&&&&&&&&&&|||||\n")
            break
        else:
            print("\n||||||||||| Invalid choice. |||||||||||")

# Start the script
if __name__ == "__main__":
    main()