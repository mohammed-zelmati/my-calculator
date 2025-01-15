# Le menu principal de choix
def main_menu():
    print("\n========== Welcome to the calculator! ===========\n")
    print("========== 1. Perform an operation   ============") # Effectuer une opération
    print("========== 2. View history ======================") # Consulter l'historique
    print("========== 3. Clear history =====================") # Vider l'historique
    print("========== 4. Exit ==============================") # Sortir de script

# Demande à l'utilisateur de rentrer deux nombres entiers ou décimales et gérer les erreurs
def get_numbers():
    while True:
        try:
            num1 = float(input("========= Enter the first number: "))
            num2 = float(input("========= Enter the second number: "))
            return num1, num2
        except ValueError:
            print("\n======= Invalid input. Please enter valid numbers. ========\n")

# Demande à l'utilisateur de rentrer un opérateur et gérer les erreurs
def get_operation():
    while True:
        operation = input("\n===== Enter the desired operation (+, -, *, /): ")
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("\n========= Invalid operation. Please enter one of the following operations: +, -, * , / : ")

# Faire les calcules de deux nombres avec deux chiffres après la firgule et gerer l'erreur de division par zéro
def calculate(num1, num2, operation):
    if operation == '+':
        sum = round(num1 + num2, 2)
        return sum
    elif operation == '-':
        sum = round(num1 - num2, 2)
        return sum
    elif operation == '*':
        sum = round(num1 * num2, 2)
        return sum
    elif operation == '/':
        if num2 != 0:
            sum = round(num1 / num2 , 2)
        return sum
    else:
        print("\n=========== Error: Division by zero. ===========\n")
        return None

# Consulter l'historique s'il existe ou s'il n'existe pas
def show_history(history):
    if history:
        print("\n=========== operations recorded. ===========\n")
        for i in history:
            print(i)
    else:
        print("\n=========== No operations recorded. ===========\n")

def clear_history():
    return []

def main():
    history = []
    while True:
        main_menu()
        choice = input(" \n========== Enter your choice (number between 1 and 4) :\n ")
        if choice == '1':
            num1, num2 = get_numbers()
            operation = get_operation()
            result = calculate(num1, num2, operation)
            if result is not None:
                print(f"\n========= The result of :\n {num1} {operation} {num2} = {result} ")
                history.append(f"{num1} {operation} {num2} = {result}")    
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            history = clear_history()
            print("\n========== The history has been cleared==========\n")
        elif choice == '4':
            print("\n=========== Goodbye!===========================\n")
            break
        else:
            print("\n=========== Invalid choice.Enter a number between 1 and 4 : ")
# Démmarer le script
if __name__ == "__main__":
    main()